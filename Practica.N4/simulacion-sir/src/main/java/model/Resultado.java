package model;

import java.util.Objects;

/**
 * Resultado inmutable que almacena la foto epidemiológica en un tiempo 't'.
 * Utilizado para la vista y la posterior exportación a CSV.
 */
public final class Resultado {
    private final int tiempo;
    private final int susceptibles;
    private final int infectados;
    private final int recuperados;

    public Resultado(int tiempo, int susceptibles, int infectados, int recuperados) {
        this.tiempo = tiempo;
        this.susceptibles = susceptibles;
        this.infectados = infectados;
        this.recuperados = recuperados;
    }

    public int tiempo() {
        return tiempo;
    }

    public int susceptibles() {
        return susceptibles;
    }

    public int infectados() {
        return infectados;
    }

    public int recuperados() {
        return recuperados;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }
        if (!(other instanceof Resultado)) {
            return false;
        }
        Resultado resultado = (Resultado) other;
        return tiempo == resultado.tiempo
                && susceptibles == resultado.susceptibles
                && infectados == resultado.infectados
                && recuperados == resultado.recuperados;
    }

    @Override
    public int hashCode() {
        return Objects.hash(tiempo, susceptibles, infectados, recuperados);
    }

    @Override
    public String toString() {
        return "Resultado[tiempo=" + tiempo
                + ", susceptibles=" + susceptibles
                + ", infectados=" + infectados
                + ", recuperados=" + recuperados + "]";
    }

    /**
     * Convierte el registro a un formato separado por comas.
     *
     * @return Cadena formateada para CSV.
     */
    public String toCSV() {
        return tiempo + "," + susceptibles + "," + infectados + "," + recuperados;
    }
}