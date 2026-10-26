package model;

/**
 * Representa un agente (persona) de la población dentro de la simulación.
 */
public class Individuo {
    private final int id;
    private Estado estado;

    public Individuo(int id, Estado estadoInicial) {
        this.id = id;
        this.estado = estadoInicial;
    }

    public int getId() {
        return id;
    }

    public Estado getEstado() {
        return estado;
    }

    public void setEstado(Estado estado) {
        this.estado = estado;
    }
}