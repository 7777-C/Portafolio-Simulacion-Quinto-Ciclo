# controllers/simulacion_controller.py
from config.parametros import P0, R, SIGMA, TIEMPO, DT, SEMILLA, DATOS_ENTRADA
from models.deterministico import ModeloDeterministico
from models.discreto import ModeloDiscreto
from models.estocastico import ModeloEstocastico
from models.continuo_euler import ModeloContinuoEuler
from views.grafica_comparativa import graficar_comparativa
from views.grafica_individual import graficar_individual
from views.tabla_resultados import mostrar_tabla


class SimulacionController:
    """Orquesta modelos y vistas."""

    def __init__(self):
        self.resultados = {}

    def ejecutar_modelos(self):
        self.resultados['Determinístico'] = ModeloDeterministico(
            P0, R, TIEMPO).simular()

        self.resultados['Discreto'] = ModeloDiscreto(
            P0, R, TIEMPO).simular()

        self.resultados['Estocástico'] = ModeloEstocastico(
            P0, R, TIEMPO, SIGMA, SEMILLA).simular()

        self.resultados['Continuo (Euler)'] = ModeloContinuoEuler(
            P0, R, TIEMPO, DT).simular()

        return self.resultados

    def mostrar_resultados(self):
        for nombre, (t, p) in self.resultados.items():
            graficar_individual(nombre, t, p, guardar=True)
        graficar_comparativa(self.resultados, guardar=True)
        mostrar_tabla(self.resultados, guardar=True)

    def resumen_numerico(self):
        print("\n=== Valores finales (t = {}) ===".format(TIEMPO))
        for nombre, (t, p) in self.resultados.items():
            print(f"  {nombre:20s} -> P_final = {p[-1]:,.2f}")

    def ejecutar(self):
        print("=" * 60)
        print(" SIMULACIÓN SEMANA 2: Comparación de modelos")
        print("=" * 60)
        print(f"Datos de entrada : {DATOS_ENTRADA}")
        print(f"P0={P0}  r={R}  sigma={SIGMA}  dt={DT}  tiempo={TIEMPO}")
        print("-" * 60)
        self.ejecutar_modelos()
        self.resumen_numerico()
        self.mostrar_resultados()
        print("\n[OK] Simulación finalizada correctamente.")