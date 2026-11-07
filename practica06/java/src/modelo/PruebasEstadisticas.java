package modelo;

import java.util.Arrays;

/** Modelo: pruebas de bondad de ajuste Chi-cuadrado y Kolmogorov-Smirnov. */
public final class PruebasEstadisticas {
    public static final double ALFA = 0.05;

    private PruebasEstadisticas() {}

    public record ResultadoChi2(int[] observadas, double esperada, double estadistico,
                                int gradosLibertad, double pValor, boolean rechazaH0) {}

    public record ResultadoKS(double dMas, double dMenos, double estadistico,
                              double pValor, boolean rechazaH0, double[] ordenados) {}

    public static ResultadoChi2 chiCuadrado(double[] datos, int k) {
        int n = datos.length;
        double esperada = (double) n / k;
        int[] observadas = new int[k];
        for (double u : datos) {
            int idx = Math.min((int) (u * k), k - 1);
            observadas[idx]++;
        }
        double chi2 = 0.0;
        for (int o : observadas) chi2 += Math.pow(o - esperada, 2) / esperada;
        int gl = k - 1;
        double p = FuncionesEspeciales.pValorChi2(chi2, gl);
        return new ResultadoChi2(observadas, esperada, chi2, gl, p, p < ALFA);
    }

    public static ResultadoKS kolmogorovSmirnov(double[] datos) {
        double[] ord = datos.clone();
        Arrays.sort(ord);
        int n = ord.length;
        double dMas = 0.0, dMenos = 0.0;
        for (int i = 1; i <= n; i++) {
            double fTeorica = ord[i - 1];                 // F(x) = x en U(0,1)
            dMas = Math.max(dMas, (double) i / n - fTeorica);
            dMenos = Math.max(dMenos, fTeorica - (double) (i - 1) / n);
        }
        double d = Math.max(dMas, dMenos);
        double p = FuncionesEspeciales.pValorKS(d, n);
        return new ResultadoKS(dMas, dMenos, d, p, p < ALFA, ord);
    }
}
