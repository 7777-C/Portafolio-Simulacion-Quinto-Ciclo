package model;

/**
 * Representa los estados epidemiológicos posibles en el modelo SIR.
 */
public enum Estado {
    /** Persona propensa a contagiarse. */
    SUSCEPTIBLE,
    
    /** Persona infectada capaz de propagar el virus. */
    INFECTADO,
    
    /** Persona recuperada con inmunidad permanente. */
    RECUPERADO
}