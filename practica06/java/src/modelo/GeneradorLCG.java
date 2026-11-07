package modelo;

/**
 * Modelo: Generador Congruencial Lineal (LCG).
 * X(n+1) = (a * X(n) + c) mod m      U(n+1) = X(n+1) / m
 */
public class GeneradorLCG {
    private final String nombre;
    private final long semilla, a, c, m;
    private long x;

    public GeneradorLCG(long semilla, long a, long c, long m, String nombre) {
        this.nombre = nombre;
        this.semilla = semilla;
        this.a = a;
        this.c = c;
        this.m = m;
        this.x = semilla;
    }

    public void reiniciar() {
        x = semilla;
    }

    /** Siguiente número pseudoaleatorio en [0,1). */
    public double siguiente() {
        x = (a * x + c) % m;
        return (double) x / m;
    }

    /** Genera n números desde la semilla (reinicia el generador). */
    public double[] generar(int n) {
        reiniciar();
        double[] datos = new double[n];
        for (int i = 0; i < n; i++) datos[i] = siguiente();
        return datos;
    }

    public String getNombre() { return nombre; }

    public String descripcion() {
        return String.format("%s: semilla=%d, a=%d, c=%d, m=%d", nombre, semilla, a, c, m);
    }
}
