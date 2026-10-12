# views/grafica_individual.py
import os
import matplotlib.pyplot as plt
from config.parametros import RUTA_FIGURAS


def graficar_individual(nombre, t, p, guardar=True):
    plt.figure(figsize=(9, 5))
    plt.plot(t, p, color='tab:purple', lw=2)
    plt.title(f'Modelo {nombre}')
    plt.xlabel('Tiempo')
    plt.ylabel('Población')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    if guardar:
        os.makedirs(RUTA_FIGURAS, exist_ok=True)
        archivo = os.path.join(
            RUTA_FIGURAS,
            f"{nombre.lower().replace(' ', '_').replace('(', '').replace(')', '')}.png"
        )
        plt.savefig(archivo, dpi=150)
        print(f"[OK] Figura guardada en {archivo}")
    plt.show()