# Práctica 07 - Estimación de π con el método de Monte Carlo
Asignatura: Simulación · Carrera de Computación · UNL

Implementación en **Python** y **Java** con arquitectura **Modelo-Vista-Controlador (MVC)**.

## Estructura

```
practica07_montecarlo/
├── python/
│   ├── main.py                          # Punto de entrada
│   ├── model/                           # MODELO
│   │   ├── lcg_random.py                #   Generador pseudoaleatorio (LCG 48 bits)
│   │   ├── monte_carlo_model.py         #   Lógica: π ≈ 4·Nc/N
│   │   └── resultado.py                 #   Estructura de datos del resultado
│   ├── view/                            # VISTA
│   │   ├── console_view.py              #   Tabla por consola + exportar CSV
│   │   └── plot_view.py                 #   Gráficos (Matplotlib)
│   └── controller/
│       └── experiment_controller.py     # CONTROLADOR (ejecuta y mide tiempos)
├── java/
│   └── src/
│       ├── Main.java                    # Punto de entrada
│       ├── model/  LcgRandom, MonteCarloModel, Resultado
│       ├── view/   ConsoleView
│       └── controller/ ExperimentController
├── comparar_resultados.py               # Une los CSV y arma la tabla de la guía
└── resultados/                          # Aquí se guardan CSV y gráficos
```

## Requisitos
- Python 3.8+ (Matplotlib es opcional, solo para los gráficos)
- JDK 17 o superior (usa `record`)

## Ejecución

**1. Python** (desde la carpeta `python/`):
```
cd python
python main.py          # semilla por defecto: 42
python main.py 123      # semilla personalizada
```

**2. Java** (desde la carpeta `java/`):
```
cd java
mkdir out
javac -encoding UTF-8 -d out src/Main.java src/model/*.java src/view/*.java src/controller/*.java
java -cp out Main        # semilla por defecto: 42
java -cp out Main 123    # semilla personalizada
```
En Windows (CMD) reemplace `src/model/*.java` etc. por la lista de archivos si el comodín falla,
o simplemente abra la carpeta `java/src` en IntelliJ IDEA / Eclipse / NetBeans y ejecute `Main`.

**3. Comparar** (desde la raíz del proyecto, con la MISMA semilla en ambos):
```
python comparar_resultados.py
```
Genera `resultados/tabla_comparativa.csv` con las columnas:
`N | π estimado | Error | Tiempo Python | Tiempo Java | Misma secuencia`

## ¿Por qué ambos programas dan la misma secuencia?
La guía pide "dos implementaciones que produzcan la misma secuencia con los mismos parámetros".
Para lograrlo, el generador `LcgRandom` está implementado de forma idéntica en ambos lenguajes
(congruencial lineal de 48 bits, el mismo algoritmo de `java.util.Random`):

    X(n+1) = (0x5DEECE66D · X(n) + 0xB) mod 2^48

Con la misma semilla, Nc y π estimado coinciden exactamente. Lo único que cambia entre
lenguajes es el **tiempo de ejecución** (pregunta 4 y 5 de la guía).
Si se usara `random` de Python y `Random` de Java sin esto, las secuencias serían distintas.

## Método
Se generan N puntos (x, y) uniformes en [-1, 1]² y se cuenta cuántos caen dentro del círculo
unitario (x² + y² ≤ 1). Entonces **π ≈ 4 · Nc / N**. Tamaños de muestra: 1 000, 10 000,
100 000 y 1 000 000.

## Salidas (carpeta `resultados/`)
- `resultados_python.csv`, `resultados_java.csv`
- `tabla_comparativa.csv`
- `puntos_montecarlo.png` (2 000 puntos dentro/fuera del círculo)
- `error_vs_n.png` (error vs. N, con referencia 1/√N)

## Nota
Los tiempos dependen de su computador; ejecute cada programa varias veces y use sus propios
valores en el informe. Las conclusiones y respuestas a las preguntas de análisis y de control
deben ser redactadas por usted a partir de sus resultados.
