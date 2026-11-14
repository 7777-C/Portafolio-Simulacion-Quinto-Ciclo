package model;

/** MODELO - Resultado de un experimento. */
public record Resultado(int n, double piEstimado, long puntosDentro,
                        double errorAbsoluto, double tiempoMs) { }
