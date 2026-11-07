import controlador.Controlador;
import vista.VistaConsola;

/** Práctica 06 - Validación estadística de números pseudoaleatorios (Java). */
public class Main {
    public static void main(String[] args) {
        new Controlador(new VistaConsola(), "salida").ejecutarTodo();
    }
}
