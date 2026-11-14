package model;

/**
 * MODELO - Generador pseudoaleatorio LCG de 48 bits.
 * Mismo algoritmo que java.util.Random y que lcg_random.py (Python),
 * por lo que con la misma semilla ambas implementaciones generan la misma secuencia.
 *
 *   X(n+1) = (a * X(n) + c) mod 2^48 ; a = 0x5DEECE66D, c = 0xB
 */
public class LcgRandom {
    private static final long MULTIPLIER = 0x5DEECE66DL;
    private static final long ADDEND = 0xBL;
    private static final long MASK = (1L << 48) - 1;

    private long seed;

    public LcgRandom(long seed) {
        this.seed = (seed ^ MULTIPLIER) & MASK;
    }

    private int next(int bits) {
        seed = (seed * MULTIPLIER + ADDEND) & MASK;
        return (int) (seed >>> (48 - bits));
    }

    /** Número uniforme en [0, 1) con 53 bits de precisión. */
    public double nextDouble() {
        return (((long) next(26) << 27) + next(27)) * (1.0 / (1L << 53));
    }
}
