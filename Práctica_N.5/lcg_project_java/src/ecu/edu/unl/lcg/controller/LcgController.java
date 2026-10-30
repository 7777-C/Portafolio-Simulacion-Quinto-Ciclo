package ecu.edu.unl.lcg.controller;

import ecu.edu.unl.lcg.model.LcgModel;
import ecu.edu.unl.lcg.view.LcgView;
import java.util.List;

public class LcgController {
    private LcgModel model;
    private LcgView view;

    public LcgController(long seed) {
        this.model = new LcgModel(seed);
        this.view = new LcgView();
    }

    public void runSimulation(int totalSamples, int previewCount) {
        System.out.println("--- RESULTADOS LCG JAVA (Semilla: " + model.getSeed() + ") ---");
        List<double[]> results = model.generateSequence(totalSamples);
        view.printTable(results, previewCount);
    }
}
