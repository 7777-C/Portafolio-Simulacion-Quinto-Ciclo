"""Vista: salida por consola y gráficos (matplotlib)."""
import os


class VistaConsola:
    def titulo(self, texto: str) -> None:
        print("\n" + "=" * 78)
        print(texto)
        print("=" * 78)

    def mostrar_secuencia(self, datos: list[float], cuantos: int = 10) -> None:
        print(f"Primeros {cuantos} números generados:")
        print("  " + ", ".join(f"{u:.8f}" for u in datos[:cuantos]))
        print(f"Total generados: {len(datos)}")

    def mostrar_chi2(self, r, k: int = 10) -> None:
        print("\n--- Prueba Chi-cuadrado ---")
        print(f"{'Intervalo':<16}{'Observada':>12}{'Esperada':>12}")
        for i, o in enumerate(r.observadas):
            print(f"[{i / k:.1f}, {(i + 1) / k:.1f}){'':<5}{o:>12}{r.esperada:>12.1f}")
        print(f"Chi² = {r.estadistico:.4f} | gl = {r.grados_libertad} | p = {r.p_valor:.6f}")
        self._decision(r.rechaza_h0)

    def mostrar_ks(self, r) -> None:
        print("\n--- Prueba Kolmogorov-Smirnov ---")
        print(f"D+ = {r.d_mas:.6f} | D- = {r.d_menos:.6f}")
        print(f"D  = {r.estadistico:.6f} | p = {r.p_valor:.6f}")
        self._decision(r.rechaza_h0)

    def _decision(self, rechaza: bool) -> None:
        if rechaza:
            print("Decisión (α=0.05): p < 0.05 -> SE RECHAZA H0 (no es uniforme).")
        else:
            print("Decisión (α=0.05): p >= 0.05 -> NO SE RECHAZA H0 (compatible con U(0,1)).")

    def mostrar_comparacion(self, filas: list[tuple]) -> None:
        print(f"\n{'Configuración':<22}{'Chi²':>10}{'p(χ²)':>12}{'Dec.':>10}"
              f"{'D (KS)':>10}{'p(KS)':>12}{'Dec.':>10}")
        for nombre, c, k in filas:
            dc = "Rechaza" if c.rechaza_h0 else "No rech."
            dk = "Rechaza" if k.rechaza_h0 else "No rech."
            print(f"{nombre:<22}{c.estadistico:>10.3f}{c.p_valor:>12.5f}{dc:>10}"
                  f"{k.estadistico:>10.5f}{k.p_valor:>12.5f}{dk:>10}")

    def mostrar_tabla_pi(self, filas) -> None:
        print(f"\n{'N':>10}{'π estimado':>14}{'Error':>14}{'Tiempo Python (s)':>20}")
        for r in filas:
            print(f"{r.n:>10}{r.pi_estimado:>14.6f}{r.error:>14.6f}{r.tiempo_s:>20.4f}")

    def mensaje(self, texto: str) -> None:
        print(texto)

    # ---------------- gráficos ----------------
    def graficar(self, datos, chi2, ks, ruta: str, titulo: str) -> None:
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
        except ImportError:
            print("matplotlib no disponible: se omite el gráfico.")
            return
        k = len(chi2.observadas)
        fig, ejes = plt.subplots(1, 2, figsize=(12, 4.5))
        ejes[0].bar(range(k), chi2.observadas, color="#3b6ea5", label="Observada")
        ejes[0].axhline(chi2.esperada, color="red", linestyle="--", label="Esperada")
        ejes[0].set_xticks(range(k))
        ejes[0].set_xticklabels([f"{i / k:.1f}" for i in range(k)])
        ejes[0].set_title("Histograma (Chi-cuadrado)")
        ejes[0].legend()

        n = len(ks.ordenados)
        paso = max(1, n // 2000)               # submuestreo para graficar
        xs = ks.ordenados[::paso]
        emp = [(i * paso + 1) / n for i in range(len(xs))]
        ejes[1].step(xs, emp, where="post", label="F_n(x) empírica")
        ejes[1].plot([0, 1], [0, 1], "r--", label="F(x) teórica U(0,1)")
        ejes[1].set_title(f"FDA acumulada (KS: D={ks.estadistico:.4f})")
        ejes[1].legend()
        fig.suptitle(titulo)
        fig.tight_layout()
        os.makedirs(os.path.dirname(ruta) or ".", exist_ok=True)
        fig.savefig(ruta, dpi=120)
        plt.close(fig)
        print(f"Gráfico guardado en: {ruta}")
