from modelo.modelo_lluvia import ModeloLluvia
from modelo.estrategias import TemperaturaInterpolada, ClasificacionEstandar
from vista.vista_lluvia import VistaLluvia


class ControladorLluvia:

    def __init__(self, modelo: ModeloLluvia, vista: VistaLluvia):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self, horas, humedad, nubosidad, temperatura):
        self.vista.mostrar_mensaje("Iniciando simulación de lluvia...\n")

        # 1. El Modelo procesa los datos
        resultados = self.modelo.procesar(horas, humedad, nubosidad, temperatura)

        # 2. La Vista los muestra
        self.vista.mostrar_tabla(resultados)
        self.vista.mostrar_grafica(resultados)

        self.vista.mostrar_mensaje("\nSimulación finalizada.")