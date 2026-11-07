package controlador;

import modelo.GeneradorLCG;
import modelo.MonteCarloPi;
import modelo.MonteCarloPi.ResultadoPi;
import modelo.PruebasEstadisticas;
import modelo.PruebasEstadisticas.ResultadoChi2;
import modelo.PruebasEstadisticas.ResultadoKS;
import vista.VistaConsola;
import vista.VistaConsola.FilaComparacion;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

/** Controlador: coordina modelo y vista. */
public class Controlador {
    private final VistaConsola vista;
    private final String dirSalida;

    // Configuraciones a comparar (objetivo 5 de la guía)
    private final List<GeneradorLCG> configuraciones = List.of(
            new GeneradorLCG(12345L, 1664525L, 1013904223L, 1L << 32, "NumRecipes"),
            new GeneradorLCG(12345L, 1103515245L, 12345L, 1L << 31, "ANSI_C"),
            new GeneradorLCG(1L, 65539L, 0L, 1L << 31, "RANDU"),
            new GeneradorLCG(7L, 1229L, 1L, 2048L, "PeriodoCorto"),
            new GeneradorLCG(1L, 2L, 0L, 1L << 31, "Degenerado"));

    public Controlador(VistaConsola vista, String dirSalida) {
        this.vista = vista;
        this.dirSalida = dirSalida;
    }

    /** Actividad 1 + Algoritmo 2 + Algoritmo 3 para un generador. */
    public FilaComparacion analizarGenerador(GeneradorLCG gen, int n, int k,
                                             boolean detalle, boolean graficar) {
        double[] datos = gen.generar(n);
        ResultadoChi2 chi2 = PruebasEstadisticas.chiCuadrado(datos, k);
        ResultadoKS ks = PruebasEstadisticas.kolmogorovSmirnov(datos);
        if (detalle) {
            vista.titulo(gen.descripcion() + "  |  N = " + n);
            vista.mostrarSecuencia(datos, 10);
            vista.mostrarChi2(chi2, k);
            vista.mostrarKS(ks);
        }
        if (graficar) {
            vista.graficar(chi2, ks, dirSalida + "/java_" + gen.getNombre() + ".png", gen.descripcion());
        }
        return new FilaComparacion(gen.getNombre(), chi2, ks);
    }

    public void compararConfiguraciones(int n) {
        vista.titulo("Comparación de configuraciones del LCG (N = " + n + ")");
        List<FilaComparacion> filas = new ArrayList<>();
        for (GeneradorLCG gen : configuraciones) {
            filas.add(analizarGenerador(gen, n, 10, false, true));
        }
        vista.mostrarComparacion(filas);
    }

    public void tablaPi(int[] tamanios) {
        vista.titulo("Estimación de π (Monte Carlo con LCG) - Java");
        GeneradorLCG gen = configuraciones.get(0);
        List<ResultadoPi> filas = new ArrayList<>();
        for (int n : tamanios) filas.add(MonteCarloPi.estimar(gen, n));
        vista.mostrarTablaPi(filas);

        new File(dirSalida).mkdirs();
        String ruta = dirSalida + "/resultados_java.csv";
        try (PrintWriter w = new PrintWriter(ruta)) {
            w.println("N,pi_estimado,error,tiempo_s");
            for (ResultadoPi r : filas) {
                w.println(String.format(Locale.US, "%d,%.10f,%.10f,%.6f",
                        r.n(), r.piEstimado(), r.error(), r.tiempoS()));
            }
            vista.mensaje("CSV guardado en: " + ruta);
        } catch (IOException e) {
            vista.mensaje("No se pudo escribir el CSV: " + e.getMessage());
        }
    }

    public void ejecutarTodo() {
        // Calentamiento de la JVM (JIT) para que los tiempos sean representativos
        MonteCarloPi.estimar(configuraciones.get(0), 200_000);

        analizarGenerador(configuraciones.get(0), 10_000, 10, true, true);
        compararConfiguraciones(10_000);
        tablaPi(new int[]{1_000, 10_000, 100_000, 1_000_000});
    }
}
