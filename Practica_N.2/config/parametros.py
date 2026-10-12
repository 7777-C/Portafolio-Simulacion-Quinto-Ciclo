# Datos de entrada 
DATOS_ENTRADA = [1000, 1100, 1250, 1400, 1600, 1850, 2100]

P0 = DATOS_ENTRADA[0]      # Población inicial = 1000
R = 0.15                   # Tasa de crecimiento (15%)
SIGMA = 50                 # Desviación estándar del ruido
TIEMPO = 20                # Tiempo total de simulación
DT = 0.1                   # Tamaño de paso para Euler
SEMILLA = 42               # Semilla para reproducibilidad

# Rutas de salida
RUTA_FIGURAS = "outputs/figuras"
RUTA_CSV = "outputs/resultados.csv"