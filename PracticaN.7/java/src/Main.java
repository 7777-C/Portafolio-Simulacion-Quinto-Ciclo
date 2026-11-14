import controller.ExperimentController;
import model.MonteCarloModel;
import view.ConsoleView;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Punto de entrada (Java).
 * Uso: java Main [semilla] [carpetaResultados]
 * Ejecutar desde la carpeta java/ (por defecto guarda en ../resultados).
 */
public class Main {
    private static final int[] TAMANOS = {1_000, 10_000, 100_000, 1_000_000};
    private static final long SEMILLA_POR_DEFECTO = 42L;

    public static void main(String[] args) throws IOException {
        long semilla = args.length > 0 ? Long.parseLong(args[0]) : SEMILLA_POR_DEFECTO;
        Path carpeta = args.length > 1 ? Paths.get(args[1]) : Paths.get("resultados");
        ExperimentController controlador = new ExperimentController(new MonteCarloModel(), new ConsoleView());
        controlador.ejecutar(TAMANOS, semilla, carpeta.resolve("resultados_java.csv"));
    }
}
