package modelo;

/** Modelo: estimación de π por Monte Carlo usando pares (x, y) del LCG. */
public final class MonteCarloPi {
    private MonteCarloPi() {}

    public record ResultadoPi(int n, double piEstimado, double error, double tiempoS) {}

    public static ResultadoPi estimar(GeneradorLCG gen, int n) {
        gen.reiniciar();
        long inicio = System.nanoTime();
        long aciertos = 0;
        for (int i = 0; i < n; i++) {
            double x = gen.siguiente();
            double y = gen.siguiente();
            if (x * x + y * y <= 1.0) aciertos++;
        }
        double tiempo = (System.nanoTime() - inicio) / 1e9;
        double pi = 4.0 * aciertos / n;
        return new ResultadoPi(n, pi, Math.abs(Math.PI - pi), tiempo);
    }
}
