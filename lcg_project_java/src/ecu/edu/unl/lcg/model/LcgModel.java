package ecu.edu.unl.lcg.model;

import java.util.ArrayList;
import java.util.List;

public class LcgModel {
    private final long a = 1664525L;
    private final long c = 1013904223L;
    private final long m = 4294967296L; // 2^32 definido estrictamente como tipo long
    private long seed;
    private long state;

    public LcgModel(long seed) {
        this.seed = seed;
        this.state = seed;
    }

    public void reset(long newSeed) {
        this.seed = newSeed;
        this.state = newSeed;
    }

    public List<double[]> generateSequence(int n) {
        this.state = this.seed;
        List<double[]> sequence = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            // Formula LCG utilizando únicamente enteros (long)
            this.state = (a * this.state + c) % m;
            
            // Normalización: división en double (cast a double para no truncar a cero)
            double normalized = (double) this.state / (double) m; 
            
            sequence.add(new double[]{(double) this.state, normalized});
        }
        return sequence;
    }

    public long getSeed() { return seed; }
}