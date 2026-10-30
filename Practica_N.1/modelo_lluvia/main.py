from modelo.estrategias import TemperaturaInterpolada, ClasificacionEstandar
from modelo.modelo_lluvia import ModeloLluvia
from vista.vista_lluvia import VistaLluvia
from controlador.controlador_lluvia import ControladorLluvia
from datos.datos_entrada import DatosEntrada


def main():
    # 1. Crear las estrategias (Strategy)
    estrategia_temp = TemperaturaInterpolada()
    estrategia_clas = ClasificacionEstandar()

    # 2. Crear el Modelo (inyectando las estrategias)
    modelo = ModeloLluvia(estrategia_temp, estrategia_clas)

    # 3. Crear la Vista
    vista = VistaLluvia()

    # 4. Crear el Controlador (inyectando Modelo y Vista)
    controlador = ControladorLluvia(modelo, vista)

    # 5. Ejecutar el flujo
    controlador.ejecutar(
        DatosEntrada.HORAS,
        DatosEntrada.HUMEDAD,
        DatosEntrada.NUBOSIDAD,
        DatosEntrada.TEMPERATURA
    )


if __name__ == "__main__":
    main()