package view;

import model.Resultado;

import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;

/** VISTA - Salida por consola y exportación CSV. */
public class ConsoleView {

    public void mostrarEncabezado(long semilla, int[] tamanos) {
        System.out.println("=".repeat(78));
        System.out.println(" PRÁCTICA 07 - Estimación de π con Monte Carlo (Java)");
        System.out.println(" Semilla: " + semilla + "   Tamaños de muestra: " + Arrays.toString(tamanos));
        System.out.println("=".repeat(78));
    }

    public void mostrarTabla(List<Resultado> resultados) {
        System.out.println(String.format(Locale.US, "%12s | %12s | %10s | %12s | %12s",
                "N", "π estimado", "Nc", "Error abs.", "Tiempo (ms)"));
        System.out.println("-".repeat(70));
        for (Resultado r : resultados) {
            System.out.println(String.format(Locale.US, "%,12d | %12.6f | %,10d | %12.6f | %12.3f",
                    r.n(), r.piEstimado(), r.puntosDentro(), r.errorAbsoluto(), r.tiempoMs()));
        }
        System.out.println("-".repeat(70));
    }

    public void mostrarMensaje(String mensaje) {
        System.out.println(mensaje);
    }

    public void exportarCsv(List<Resultado> resultados, Path ruta) throws IOException {
        Files.createDirectories(ruta.toAbsolutePath().getParent());
        try (PrintWriter w = new PrintWriter(Files.newBufferedWriter(ruta, StandardCharsets.UTF_8))) {
            w.print("N,pi_estimado,puntos_dentro,error_absoluto,tiempo_ms\n");
            for (Resultado r : resultados) {
                w.print(String.format(Locale.US, "%d,%s,%d,%s,%.3f\n",
                        r.n(), Double.toString(r.piEstimado()), r.puntosDentro(),
                        Double.toString(r.errorAbsoluto()), r.tiempoMs()));
            }
        }
    }
}
