import numpy as np
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt


class VistaLluvia:
 
    def mostrar_tabla(self, resultados):
        print("=" * 95)
        print(f"{'Hora':<8}{'Hum.':<7}{'Nub.':<7}{'Temp':<7}"
              f"{'H':<7}{'N':<7}{'Tf':<7}{'I':<8}{'Estado'}")
        print("=" * 95)
        for r in resultados:
            print(f"{r['hora']:<8}{r['humedad']:<7}{r['nubosidad']:<7}"
                  f"{r['temp']:<7}{r['H']:<7.2f}{r['N']:<7.2f}"
                  f"{r['Tf']:<7.2f}{r['I']:<8.3f}{r['estado']}")
        print("=" * 95)

    def mostrar_grafica(self, resultados, archivo="grafica_lluvia.png"):
        horas = [r["hora"] for r in resultados]
        indices = [r["I"] for r in resultados]
        colores = [r["color"] for r in resultados]

        x = np.arange(len(horas))
        fig, ax = plt.subplots(figsize=(12, 6))

        ax.bar(x, indices, color=colores, edgecolor="black",
               width=0.6, label="Índice I")

        ax.axhline(0.40, color="gray", linestyle="--", linewidth=1, label="Umbral 0.40")
        ax.axhline(0.60, color="blue", linestyle="--", linewidth=1, label="Umbral 0.60")
        ax.axhline(0.75, color="red",  linestyle="--", linewidth=1, label="Umbral 0.75")

        for i, v in enumerate(indices):
            ax.text(i, v + 0.02, f"{v:.2f}", ha="center",
                    fontsize=9, fontweight="bold")

        ax.set_xlabel("Hora del día", fontsize=12)
        ax.set_ylabel("Índice de posibilidad de lluvia (I)", fontsize=12)
        ax.set_title("Modelo de Posibilidad de Lluvia\nI = 0.5H + 0.3N + 0.2Tf",
                     fontsize=14, fontweight="bold")
        ax.set_xticks(x)
        ax.set_xticklabels(horas)
        ax.set_ylim(0, 1.0)
        ax.legend(loc="upper left")
        ax.grid(axis="y", alpha=0.3)

        plt.tight_layout()
        plt.savefig(archivo, dpi=150)
        plt.close()
        print(f"\n[OK] Gráfica guardada como: {archivo}")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)