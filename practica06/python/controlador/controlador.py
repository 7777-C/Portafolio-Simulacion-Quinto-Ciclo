"""Controlador: coordina modelo y vista."""
import csv
import os

from modelo.lcg import GeneradorLCG
from modelo.monte_carlo_pi import estimar_pi
from modelo.pruebas import prueba_chi_cuadrado, prueba_ks

# Configuraciones a comparar (objetivo 5 de la guía)
CONFIGURACIONES = [
    GeneradorLCG(12345, 1664525, 1013904223, 2 ** 32, "NumRecipes"),
    GeneradorLCG(12345, 1103515245, 12345, 2 ** 31, "ANSI_C"),
    GeneradorLCG(1, 65539, 0, 2 ** 31, "RANDU"),
    GeneradorLCG(7, 1229, 1, 2048, "PeriodoCorto"),   # periodo 2048: pasa uniformidad pero es malo
    GeneradorLCG(1, 2, 0, 2 ** 31, "Degenerado"),      # converge a 0: debe rechazarse H0
]


class Controlador:
    def __init__(self, vista, dir_salida: str = "salida"):
        self.vista = vista
        self.dir_salida = dir_salida

    # Actividad 1 + Algoritmo 2 + Algoritmo 3 para un generador
    def analizar_generador(self, gen: GeneradorLCG, n: int = 10_000, k: int = 10,
                           detalle: bool = True, graficar: bool = True):
        datos = gen.generar(n)
        chi2 = prueba_chi_cuadrado(datos, k)
        ks = prueba_ks(datos)
        if detalle:
            self.vista.titulo(f"{gen.descripcion()}  |  N = {n}")
            self.vista.mostrar_secuencia(datos)
            self.vista.mostrar_chi2(chi2, k)
            self.vista.mostrar_ks(ks)
        if graficar:
            self.vista.graficar(datos, chi2, ks,
                                os.path.join(self.dir_salida, f"python_{gen.nombre}.png"),
                                gen.descripcion())
        return chi2, ks

    def comparar_configuraciones(self, n: int = 10_000):
        self.vista.titulo(f"Comparación de configuraciones del LCG (N = {n})")
        filas = []
        for gen in CONFIGURACIONES:
            c, k = self.analizar_generador(gen, n, detalle=False, graficar=True)
            filas.append((gen.nombre, c, k))
        self.vista.mostrar_comparacion(filas)

    def tabla_pi(self, tamanios=(1_000, 10_000, 100_000, 1_000_000)):
        self.vista.titulo("Estimación de π (Monte Carlo con LCG) - Python")
        gen = CONFIGURACIONES[0]
        filas = [estimar_pi(gen, n) for n in tamanios]
        self.vista.mostrar_tabla_pi(filas)
        os.makedirs(self.dir_salida, exist_ok=True)
        ruta = os.path.join(self.dir_salida, "resultados_python.csv")
        with open(ruta, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["N", "pi_estimado", "error", "tiempo_s"])
            for r in filas:
                w.writerow([r.n, f"{r.pi_estimado:.10f}", f"{r.error:.10f}", f"{r.tiempo_s:.6f}"])
        self.vista.mensaje(f"CSV guardado en: {ruta}")

    def ejecutar_todo(self):
        self.analizar_generador(CONFIGURACIONES[0], 10_000)
        self.comparar_configuraciones(10_000)
        self.tabla_pi()
