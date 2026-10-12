# views/grafica_comparativa.py
import os
import matplotlib.pyplot as plt
from config.parametros import RUTA_FIGURAS


def graficar_comparativa(resultados: dict, guardar=True):
    """
    resultados = {
        'Determinístico': (t, p),
        'Discreto': (t, p),
        'Estocástico': (t, p),
        'Continuo (Euler)': (t, p),
    }
    """
    plt.figure(figsize=(11, 6))
    estilos = {
        'Determinístico':   {'color': 'tab:blue',   'linestyle': '-',  'lw': 2},
        'Discreto':         {'color': 'tab:green',  'linestyle': '--', 'lw': 2},
        'Estocástico':      {'color': 'tab:red',    'linestyle': '-',  'lw': 2},
        'Continuo (Euler)': {'color': 'tab:orange', 'linestyle': ':',  'lw': 2.5},
    }
    for nombre, (t, p) in resultados.items():
        plt.plot(t, p, label=nombre, **estilos.get(nombre, {}))

    plt.title('Comparación de modelos de crecimiento poblacional', fontsize=13)
    plt.xlabel('Tiempo')
    plt.ylabel('Población')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    if guardar:
        os.makedirs(RUTA_FIGURAS, exist_ok=True)
        ruta = os.path.join(RUTA_FIGURAS, 'comparativa.png')
        plt.savefig(ruta, dpi=150)
        print(f"[OK] Figura guardada en {ruta}")
    plt.show()