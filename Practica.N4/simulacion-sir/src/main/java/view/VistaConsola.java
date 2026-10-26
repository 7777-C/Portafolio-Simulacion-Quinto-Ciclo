package view;

import model.Resultado;

/**
 * Componente VISTA que despliega información del modelo por consola.
 */
public class VistaConsola {

    public void mostrarInicio() {
        System.out.println("=================================================");
        System.out.println("   INICIANDO SIMULACIÓN MODELO EPIDEMIOLÓGICO SIR");
        System.out.println("=================================================");
    }

    public void mostrarPaso(Resultado res) {
        System.out.printf("Paso %3d: S = %3d | I = %3d | R = %3d%n",
                res.tiempo(), res.susceptibles(), res.infectados(), res.recuperados());
    }

    public void mostrarFin(String rutaArchivo) {
        System.out.println("=================================================");
        System.out.println("Simulación finalizada.");
        System.out.println("Archivo CSV generado: " + rutaArchivo);
        System.out.println("=================================================");
    }
}