"""VISTA - Gráficos con Matplotlib (opcional)."""
import os


class PlotView:
    def __init__(self, carpeta_salida: str):
        self.carpeta = carpeta_salida
        os.makedirs(carpeta_salida, exist_ok=True)

    def _plt(self):
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
            return plt
        except ImportError:
            print("[aviso] Matplotlib no está instalado: se omiten los gráficos.")
            return None

    def graficar_puntos(self, xs, ys, dentro, nombre="puntos_montecarlo.png"):
        plt = self._plt()
        if plt is None:
            return
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.scatter([x for x, d in zip(xs, dentro) if d],
                   [y for y, d in zip(ys, dentro) if d], s=3, c="tab:blue", label="Dentro")
        ax.scatter([x for x, d in zip(xs, dentro) if not d],
                   [y for y, d in zip(ys, dentro) if not d], s=3, c="tab:red", label="Fuera")
        ax.set_aspect("equal")
        ax.set_title(f"Monte Carlo - {len(xs)} puntos")
        ax.legend(loc="upper right")
        fig.savefig(os.path.join(self.carpeta, nombre), dpi=130, bbox_inches="tight")
        plt.close(fig)

    def graficar_error(self, resultados, nombre="error_vs_n.png"):
        plt = self._plt()
        if plt is None:
            return
        ns = [r.n for r in resultados]
        errs = [r.error_absoluto for r in resultados]
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.loglog(ns, errs, "o-", label="Error absoluto")
        ax.loglog(ns, [1.0 / (n ** 0.5) for n in ns], "--", label="Referencia 1/√N")
        ax.set_xlabel("N (puntos)")
        ax.set_ylabel("Error absoluto")
        ax.set_title("Error vs. tamaño de muestra")
        ax.grid(True, which="both", alpha=0.3)
        ax.legend()
        fig.savefig(os.path.join(self.carpeta, nombre), dpi=130, bbox_inches="tight")
        plt.close(fig)
