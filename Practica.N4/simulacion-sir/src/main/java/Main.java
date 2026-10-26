import controller.ControladorSimulacion;

/**
 * Punto de entrada principal de la aplicación en Java.
 */
public class Main {
    public static void main(String[] args) {
        // Parámetros obligatorios definidos en la guía académica:
        int poblacionTotal = 100;
        int infectadosIniciales = 5;
        double beta = 0.30;
        double gamma = 0.10;
        int pasosSimulacion = 100;

        // Instanciación y arranque del controlador del sistema
        ControladorSimulacion controlador = new ControladorSimulacion(
                poblacionTotal, 
                infectadosIniciales, 
                beta, 
                gamma, 
                pasosSimulacion
        );
        
        controlador.ejecutar();
    }
}