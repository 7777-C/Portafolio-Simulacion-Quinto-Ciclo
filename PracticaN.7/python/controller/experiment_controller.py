"""CONTROLADOR - Coordina Modelo y Vista, y mide el tiempo de ejecución."""
import os
import time

from model.monte_carlo_model import MonteCarloModel
from model.resultado import Resultado


class ExperimentController:
    def __init__(self, modelo: MonteCarloModel, vista, vista_graficos=None):
        self.modelo = modelo
        self.vista = vista
        self.vista_graficos = vista_graficos

    def ejecutar(self, tamanos, semilla: int, ruta_csv: str):
        self.vista.mostrar_encabezado(semilla, tamanos)
        resultados = []
        for n in tamanos:
            inicio = time.perf_counter()
            dentro = self.modelo.contar_puntos_dentro(n, semilla)
            pi_est = self.modelo.estimar_pi(n, dentro)
            tiempo_ms = (time.perf_counter() - inicio) * 1000.0
            resultados.append(Resultado(n, pi_est, dentro,
                                        self.modelo.error_absoluto(pi_est), tiempo_ms))

        self.vista.mostrar_tabla(resultados)
        self.vista.exportar_csv(resultados, ruta_csv)
        self.vista.mostrar_mensaje(f"CSV guardado en: {os.path.abspath(ruta_csv)}")

        if self.vista_graficos is not None:
            xs, ys, dentro = self.modelo.generar_puntos(2000, semilla)
            self.vista_graficos.graficar_puntos(xs, ys, dentro)
            self.vista_graficos.graficar_error(resultados)
            self.vista.mostrar_mensaje("Gráficos generados en la carpeta resultados/.")
        return resultados
