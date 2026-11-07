package modelo;

/** Modelo: funciones especiales para obtener valores p sin librerías externas. */
public final class FuncionesEspeciales {
    private FuncionesEspeciales() {}

    /** log Gamma(x) mediante la aproximación de Lanczos (g=7, n=9). */
    public static double lgamma(double x) {
        double[] coef = {
            0.99999999999980993, 676.5203681218851, -1259.1392167224028,
            771.32342877765313, -176.61502916214059, 12.507343278686905,
            -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7};
        if (x < 0.5) {
            return Math.log(Math.PI / Math.abs(Math.sin(Math.PI * x))) - lgamma(1 - x);
        }
        x -= 1;
        double s = coef[0];
        double t = x + 7.5;
        for (int i = 1; i < 9; i++) s += coef[i] / (x + i);
        return 0.5 * Math.log(2 * Math.PI) + (x + 0.5) * Math.log(t) - t + Math.log(s);
    }

    /** Gamma incompleta regularizada superior Q(a, x). */
    public static double gammaQ(double a, double x) {
        if (x <= 0) return 1.0;
        double gln = lgamma(a);
        if (x < a + 1.0) {                       // serie
            double ap = a, suma = 1.0 / a, delta = suma;
            for (int i = 0; i < 1000; i++) {
                ap += 1.0;
                delta *= x / ap;
                suma += delta;
                if (Math.abs(delta) < Math.abs(suma) * 1e-15) break;
            }
            return 1.0 - suma * Math.exp(-x + a * Math.log(x) - gln);
        }
        double tiny = 1e-300;                    // fracción continua (Lentz)
        double b = x + 1.0 - a, c = 1.0 / tiny, d = 1.0 / b, h = d;
        for (int i = 1; i < 1000; i++) {
            double an = -i * (i - a);
            b += 2.0;
            d = an * d + b;
            if (Math.abs(d) < tiny) d = tiny;
            c = b + an / c;
            if (Math.abs(c) < tiny) c = tiny;
            d = 1.0 / d;
            double delta = d * c;
            h *= delta;
            if (Math.abs(delta - 1.0) < 1e-15) break;
        }
        return Math.exp(-x + a * Math.log(x) - gln) * h;
    }

    /** P(X >= estadistico), X ~ Chi-cuadrado(gl). */
    public static double pValorChi2(double estadistico, int gl) {
        return gammaQ(gl / 2.0, estadistico / 2.0);
    }

    /** p-valor asintótico de Kolmogorov-Smirnov (corrección de Stephens). */
    public static double pValorKS(double d, int n) {
        if (d <= 0) return 1.0;
        double sq = Math.sqrt(n);
        double lam = (sq + 0.12 + 0.11 / sq) * d;
        double suma = 0.0;
        for (int k = 1; k <= 100; k++) {
            double termino = 2.0 * (k % 2 == 1 ? 1 : -1) * Math.exp(-2.0 * k * k * lam * lam);
            suma += termino;
            if (Math.abs(termino) < 1e-16) break;
        }
        return Math.min(1.0, Math.max(0.0, suma));
    }
}
