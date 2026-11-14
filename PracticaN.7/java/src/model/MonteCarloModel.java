package model;

/**
 * MODELO - Método de Monte Carlo para estimar π.
 * Puntos uniformes en [-1,1]x[-1,1]; dentro del círculo si x²+y² <= 1.
 *   π ≈ 4 · (Nc / N)
 */
public class MonteCarloModel {
    public static final double PI_REAL = Math.PI;

    public long contarPuntosDentro(int n, long semilla) {
        LcgRandom rng = new LcgRandom(semilla);
        long dentro = 0;
        for (int i = 0; i < n; i++) {
            double x = 2.0 * rng.nextDouble() - 1.0;
            double y = 2.0 * rng.nextDouble() - 1.0;
            if (x * x + y * y <= 1.0) {
                dentro++;
            }
        }
        return dentro;
    }

    public double estimarPi(int n, long puntosDentro) {
        return 4.0 * puntosDentro / n;
    }

    public double errorAbsoluto(double piEstimado) {
        return Math.abs(piEstimado - PI_REAL);
    }
}
