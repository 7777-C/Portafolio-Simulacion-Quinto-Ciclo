"""
Punto de entrada (Python).
Uso:  python main.py [semilla]
"""
import os
import sys

from controller.experiment_controller import ExperimentController
from model.monte_carlo_model import MonteCarloModel
from view.console_view import ConsoleView
from view.plot_view import PlotView

TAMANOS = [1_000, 10_000, 100_000, 1_000_000]
SEMILLA_POR_DEFECTO = 42

if __name__ == "__main__":
    semilla = int(sys.argv[1]) if len(sys.argv) > 1 else SEMILLA_POR_DEFECTO
    base = os.path.dirname(os.path.abspath(__file__))
    carpeta = os.path.join(base, "..", "resultados")

    controlador = ExperimentController(
        MonteCarloModel(), ConsoleView(), PlotView(carpeta))
    controlador.ejecutar(TAMANOS, semilla, os.path.join(carpeta, "resultados_python.csv"))
