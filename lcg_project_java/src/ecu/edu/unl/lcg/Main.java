package ecu.edu.unl.lcg;

import ecu.edu.unl.lcg.controller.LcgController;
import ecu.edu.unl.lcg.model.LcgModel;
import ecu.edu.unl.lcg.view.LcgView;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        LcgModel model = new LcgModel(12345L);
        LcgView view = new LcgView();
        
        List<double[]> results = model.generateSequence(10000);
        view.printTable(results, 20);
        
        // Guardar CSV
        view.exportToCSV(results, "datos_java.csv");
    }
}