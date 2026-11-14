"""
Compara los CSV generados por Python y Java y arma la tabla final de la guía:
    N | π estimado | Error | Tiempo Python | Tiempo Java
Además verifica que ambas implementaciones produzcan la misma secuencia
(mismo Nc y mismo π estimado).

Uso:  python comparar_resultados.py
"""
import csv
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "resultados")


def leer(nombre):
    with open(os.path.join(RES, nombre), newline="", encoding="utf-8") as f:
        return {int(r["N"]): r for r in csv.DictReader(f)}


def main():
    try:
        py = leer("resultados_python.csv")
        jv = leer("resultados_java.csv")
    except FileNotFoundError as e:
        print(f"Falta un archivo: {e.filename}\nEjecute primero ambos programas (ver README.md).")
        return

    print(f"{'N':>10} | {'π estimado':>11} | {'Error':>10} | {'T. Python (ms)':>14} | {'T. Java (ms)':>12} | Misma secuencia")
    print("-" * 85)
    filas = []
    todo_igual = True
    for n in sorted(py):
        p, j = py[n], jv[n]
        igual = (p["puntos_dentro"] == j["puntos_dentro"]
                 and abs(float(p["pi_estimado"]) - float(j["pi_estimado"])) < 1e-12)
        todo_igual &= igual
        filas.append([n, p["pi_estimado"], p["error_absoluto"], p["tiempo_ms"], j["tiempo_ms"], "SI" if igual else "NO"])
        print(f"{n:>10,} | {float(p['pi_estimado']):>11.6f} | {float(p['error_absoluto']):>10.6f} | "
              f"{float(p['tiempo_ms']):>14.3f} | {float(j['tiempo_ms']):>12.3f} | {'SI' if igual else 'NO'}")

    with open(os.path.join(RES, "tabla_comparativa.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["N", "pi_estimado", "error", "tiempo_python_ms", "tiempo_java_ms", "misma_secuencia"])
        w.writerows(filas)

    print("\nResultado:", "Ambas implementaciones generan la MISMA secuencia." if todo_igual
          else "ATENCIÓN: hay diferencias entre Python y Java.")
    print("Tabla guardada en resultados/tabla_comparativa.csv")


if __name__ == "__main__":
    main()
