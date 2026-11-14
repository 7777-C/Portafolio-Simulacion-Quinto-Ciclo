"""VISTA - Salida por consola y exportación CSV."""
import csv
import os


class ConsoleView:
    def mostrar_encabezado(self, semilla: int, tamanos):
        print("=" * 78)
        print(" PRÁCTICA 07 - Estimación de π con Monte Carlo (Python)")
        print(f" Semilla: {semilla}   Tamaños de muestra: {list(tamanos)}")
        print("=" * 78)

    def mostrar_tabla(self, resultados):
        print(f"{'N':>12} | {'π estimado':>12} | {'Nc':>10} | {'Error abs.':>12} | {'Tiempo (ms)':>12}")
        print("-" * 70)
        for r in resultados:
            print(f"{r.n:>12,} | {r.pi_estimado:>12.6f} | {r.puntos_dentro:>10,} | "
                  f"{r.error_absoluto:>12.6f} | {r.tiempo_ms:>12.3f}")
        print("-" * 70)

    def mostrar_mensaje(self, mensaje: str):
        print(mensaje)

    def exportar_csv(self, resultados, ruta: str):
        os.makedirs(os.path.dirname(os.path.abspath(ruta)), exist_ok=True)
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["N", "pi_estimado", "puntos_dentro", "error_absoluto", "tiempo_ms"])
            for r in resultados:
                w.writerow([r.n, repr(r.pi_estimado), r.puntos_dentro,
                            repr(r.error_absoluto), f"{r.tiempo_ms:.3f}"])
