# views/tabla_resultados.py
import os
import pandas as pd
from config.parametros import RUTA_CSV


def mostrar_tabla(resultados: dict, guardar=True):
    """Muestra y guarda una tabla comparativa con Pandas."""
    df = pd.DataFrame({
        nombre: pd.Series(p) for nombre, (t, p) in resultados.items()
    })
    print("\n=== Tabla comparativa (primeras 10 filas) ===")
    print(df.head(10))

    if guardar:
        os.makedirs(os.path.dirname(RUTA_CSV), exist_ok=True)
        df.to_csv(RUTA_CSV, index=False)
        print(f"\n[OK] Resultados guardados en {RUTA_CSV}")
    return df