package controller;

import model.ModeloSIR;
import model.Resultado;
import view.VistaConsola;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Componente CONTROLADOR que coordina la ejecución de la simulación
 * y la escritura de los resultados en disco.
 */
public class ControladorSimulacion {
    private final ModeloSIR modelo;
    private final VistaConsola vista;
    private final int pasosTotales;
    private final List<Resultado> historialResultados;

    public ControladorSimulacion(int poblacion, int infectadosIniciales, double beta, double gamma, int pasosTotales) {
        this.modelo = new ModeloSIR(poblacion, infectadosIniciales, beta, gamma);
        this.vista = new VistaConsola();
        this.pasosTotales = pasosTotales;
        this.historialResultados = new ArrayList<>();
    }

    public void ejecutar() {
        vista.mostrarInicio();

        // Registrar estado inicial (Paso 0)
        Resultado estadoInicial = modelo.obtenerResultadoActual();
        historialResultados.add(estadoInicial);
        vista.mostrarPaso(estadoInicial);

        // Bucle de 1 a 100 pasos
        for (int paso = 1; paso <= pasosTotales; paso++) {
            modelo.avanzarPaso();
            Resultado res = modelo.obtenerResultadoActual();
            historialResultados.add(res);
            vista.mostrarPaso(res);
        }

        String nombreArchivo = System.getProperty("user.dir") + "/resultados_java.csv";
        
        guardarCSV(nombreArchivo);
        vista.mostrarFin(nombreArchivo);
    }

    /**
     * Exporta el historial de la simulación al archivo CSV requerido.
     */
    private void guardarCSV(String nombreArchivo) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(nombreArchivo))) {
            // Escribir encabezado
            writer.write("tiempo,susceptibles,infectados,recuperados");
            writer.newLine();

            // Escribir datos de cada paso
            for (Resultado res : historialResultados) {
                writer.write(res.toCSV());
                writer.newLine();
            }
        } catch (IOException e) {
            System.err.println("Error al guardar el archivo CSV: " + e.getMessage());
        }
    }
}