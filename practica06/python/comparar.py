"""Une resultados_python.csv y resultados_java.csv en la tabla de la guía.
Uso: python comparar.py   (ejecutar después de correr ambos programas)"""
import csv
import os


def leer(ruta):
    with open(ruta) as f:
        return {int(r["N"]): r for r in csv.DictReader(f)}


ruta_java = next(r for r in ("../java/salida/resultados_java.csv",
                             "salida/resultados_java.csv") if os.path.exists(r))
py = leer("salida/resultados_python.csv")
ja = leer(ruta_java)

print(f"{'N':>10}{'π Python':>13}{'π Java':>13}{'Error':>12}"
      f"{'T. Python (s)':>15}{'T. Java (s)':>13}{'Igual?':>8}")
for n in sorted(py):
    p, j = py[n], ja[n]
    igual = "SI" if p["pi_estimado"] == j["pi_estimado"] else "NO"
    print(f"{n:>10}{float(p['pi_estimado']):>13.6f}{float(j['pi_estimado']):>13.6f}"
          f"{float(p['error']):>12.6f}{float(p['tiempo_s']):>15.4f}"
          f"{float(j['tiempo_s']):>13.4f}{igual:>8}")
