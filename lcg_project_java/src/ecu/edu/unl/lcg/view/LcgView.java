package ecu.edu.unl.lcg.view;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

public class LcgView {

    public void printTable(List<double[]> data, int count) {
        System.out.printf("\n%-5s | %-15s | %-20s\n", "i", "X_i (Entero)", "U_i (Normalizado)");
        System.out.println("----------------------------------------------");
        int limit = Math.min(count, data.size());
        for (int i = 0; i < limit; i++) {
            double[] row = data.get(i);
            System.out.printf("%-5d | %-15.0f | %-20.8f\n", (i + 1), row[0], row[1]);
        }
    }

    public void exportToCSV(List<double[]> data, String filePath) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(filePath))) {
            writer.println("i,X_int,U_norm");
            for (int i = 0; i < data.size(); i++) {
                double[] row = data.get(i);
                writer.printf("%d,%.0f,%.8f\n", (i + 1), row[0], row[1]);
            }
            System.out.println("\n[JAVA] Datos exportados exitosamente a: " + filePath);
        } catch (IOException e) {
            System.err.println("Error al exportar datos: " + e.getMessage());
        }
    }
}