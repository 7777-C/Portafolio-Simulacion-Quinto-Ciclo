package model;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;

/**
 * Lógica de negocio (MODELO) que simula la interacción de la población paso a paso.
 */
public class ModeloSIR {
    private final int poblacionTotal;
    private final double beta;   // Tasa de transmisión
    private final double gamma;  // Tasa de recuperación
    private final List<Individuo> poblacion;
    private final Random random;
    private int tiempoActual;

    public ModeloSIR(int poblacionTotal, int infectadosIniciales, double beta, double gamma) {
        this.poblacionTotal = poblacionTotal;
        this.beta = beta;
        this.gamma = gamma;
        this.poblacion = new ArrayList<>(poblacionTotal);
        this.random = new Random();
        this.tiempoActual = 0;

        inicializarPoblacion(infectadosIniciales);
    }

    private void inicializarPoblacion(int infectadosIniciales) {
        for (int i = 0; i < poblacionTotal; i++) {
            if (i < infectadosIniciales) {
                poblacion.add(new Individuo(i, Estado.INFECTADO));
            } else {
                poblacion.add(new Individuo(i, Estado.SUSCEPTIBLE));
            }
        }
    }

    /**
     * Avanza un paso discreto (tick) evaluando contagios y recuperaciones.
     */
    public void avanzarPaso() {
        List<Estado> estadosAnteriores = poblacion.stream()
                .map(Individuo::getEstado)
                .collect(Collectors.toList());

        List<Integer> susceptibles = new ArrayList<>();
        List<Integer> infectados = new ArrayList<>();

        for (int i = 0; i < poblacionTotal; i++) {
            if (estadosAnteriores.get(i) == Estado.SUSCEPTIBLE) {
                susceptibles.add(i);
            } else if (estadosAnteriores.get(i) == Estado.INFECTADO) {
                infectados.add(i);
            }
        }

        // 1. LÓGICA DE CONTAGIO (Probabilidad Beta)
        for (Integer idInfectado : infectados) {
            for (Integer idSusceptible : susceptibles) {
                if (poblacion.get(idSusceptible).getEstado() == Estado.SUSCEPTIBLE) {
                    // Evaluación estocástica: si el aleatorio < Beta (0.30), se contagia
                    if (random.nextDouble() < beta) {
                        poblacion.get(idSusceptible).setEstado(Estado.INFECTADO);
                    }
                }
            }
        }

        // 2. LÓGICA DE RECUPERACIÓN (Probabilidad Gamma)
        for (Integer idInfectado : infectados) {
            // Evaluación estocástica: si el aleatorio < Gamma (0.10), se recupera
            if (random.nextDouble() < gamma) {
                poblacion.get(idInfectado).setEstado(Estado.RECUPERADO);
            }
        }

        tiempoActual++;
    }

    public Resultado obtenerResultadoActual() {
        int s = 0, i = 0, r = 0;
        for (Individuo ind : poblacion) {
            switch (ind.getEstado()) {
                case SUSCEPTIBLE:
                    s++;
                    break;
                case INFECTADO:
                    i++;
                    break;
                case RECUPERADO:
                    r++;
                    break;
            }
        }
        return new Resultado(tiempoActual, s, i, r);
    }
}