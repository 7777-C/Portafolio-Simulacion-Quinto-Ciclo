package controller;

import model.MonteCarloModel;
import model.Resultado;
import view.ConsoleView;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

/** CONTROLADOR - Coordina Modelo y Vista, y mide el tiempo de ejecución. */
public class ExperimentController {
    private final MonteCarloModel modelo;
    private final ConsoleView vista;

    public ExperimentController(MonteCarloModel modelo, ConsoleView vista) {
        this.modelo = modelo;
        this.vista = vista;
    }

    public List<Resultado> ejecutar(int[] tamanos, long semilla, Path rutaCsv) throws IOException {
        vista.mostrarEncabezado(semilla, tamanos);
        List<Resultado> resultados = new ArrayList<>();
        for (int n : tamanos) {
            long inicio = System.nanoTime();
            long dentro = modelo.contarPuntosDentro(n, semilla);
            double piEst = modelo.estimarPi(n, dentro);
            double tiempoMs = (System.nanoTime() - inicio) / 1_000_000.0;
            resultados.add(new Resultado(n, piEst, dentro, modelo.errorAbsoluto(piEst), tiempoMs));
        }
        vista.mostrarTabla(resultados);
        vista.exportarCsv(resultados, rutaCsv);
        vista.mostrarMensaje("CSV guardado en: " + rutaCsv.toAbsolutePath().normalize());
        return resultados;
    }
}
