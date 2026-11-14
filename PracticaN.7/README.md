# Práctica 07 · Estimación de π con el método de Monte Carlo

**Asignatura:** Simulación · **Ciclo:** 5 · **Carrera de Computación** · Universidad Nacional de Loja
**Docente:** José O. Guamán Q. · **Unidad 2:** Generación de números pseudoaleatorios y generación de variables aleatorias

---

## 1. Descripción del proyecto

**Propósito.** Aplicar el método de Monte Carlo para aproximar el valor de π mediante experimentos aleatorios, y analizar cómo influye el tamaño de la muestra en el error.

**Problema que resuelve.** Se generan *N* puntos (x, y) uniformes en el cuadrado [−1, 1] × [−1, 1]. Un punto está dentro del círculo unitario si x² + y² ≤ 1. Como el área del círculo es π/4 del área del cuadrado:

```
π ≈ 4 · (Nc / N)
```

donde `Nc` es el número de puntos dentro del círculo y `N` el total de puntos.

El experimento se implementa en **Python** y en **Java**, y ambos programas producen **exactamente la misma secuencia** de números (mismo generador y misma semilla), de modo que sus resultados numéricos son idénticos y solo cambia el tiempo de ejecución.

**Objetivos de la práctica**
1. Implementar un experimento Monte Carlo.
2. Analizar la influencia del tamaño de muestra sobre el error.
3. Comparar los resultados obtenidos en Python y Java.

---

## 2. Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python 3 | Implementación en Python (biblioteca estándar: `math`, `time`, `csv`, `dataclasses`) |
| Matplotlib | Gráficos (opcional; si no está instalado, se omiten) |
| Java (JDK 17 o superior) | Implementación en Java (usa `record`) |
| Visual Studio Code | Editor y terminal de ejecución |
| Generador LCG de 48 bits | Números pseudoaleatorios, programado igual en ambos lenguajes |

> NumPy y Pandas aparecen en la guía, pero no son necesarios: el generador y el conteo se programaron con la biblioteca estándar para poder reproducir la misma secuencia en Java.

**Arquitectura:** Modelo–Vista–Controlador (MVC) en ambos lenguajes.

---

## 3. Instalación

1. Descomprima el proyecto y abra la carpeta `practica07_montecarlo` en una terminal o en VS Code.
2. Verifique que tiene Python y el JDK:

   ```
   python --version
   java -version
   javac -version
   ```

   En Windows, si `python` no se reconoce, use `py`.
3. (Opcional) Instale Matplotlib para generar los gráficos:

   ```
   pip install matplotlib
   ```

---

## 4. Configuración

| Parámetro | Valor por defecto | Dónde cambiarlo |
|---|---|---|
| Semilla | `42` | Argumento al ejecutar (`python main.py 123`, `java -cp out Main 123`) |
| Tamaños de muestra | 1 000, 10 000, 100 000, 1 000 000 | Constante `TAMANOS` en `python/main.py` y `java/src/Main.java` |
| Carpeta de resultados | `resultados/` (en la raíz del proyecto) | Segundo argumento en Java (ver más abajo) |

> **Importante:** para que la comparación sea válida, use **la misma semilla** en Python y en Java.

---

## 5. Uso

### 5.1 Ejecutar Python

```
cd python
python main.py          # semilla 42
python main.py 123      # semilla personalizada
cd ..
```

Genera `resultados/resultados_python.csv` y los gráficos `puntos_montecarlo.png` y `error_vs_n.png`.

### 5.2 Ejecutar Java

**Windows (PowerShell)**

```
cd java
mkdir out
javac -encoding UTF-8 -d out (Get-ChildItem -Recurse src -Filter *.java).FullName
java -cp out Main                       # semilla 42
java -cp out Main 123                   # semilla personalizada
cd ..
```

**Linux / macOS**

```
cd java
mkdir -p out
javac -encoding UTF-8 -d out $(find src -name "*.java")
java -cp out Main
cd ..
```

**Desde un IDE (VS Code, IntelliJ, Eclipse o NetBeans):** abra `java/src` y ejecute `Main`.

Genera `resultados_java.csv`. Por defecto se guarda en `..\resultados` **relativo al directorio de trabajo**. Si lo ejecuta desde un IDE, el archivo puede quedar en otra carpeta; en ese caso pase la ruta como segundo argumento:

```
java -cp out Main 42 ..\resultados
```

o copie el CSV a la carpeta `resultados/` del proyecto.

### 5.3 Comparar resultados

Desde la raíz del proyecto, con ambos CSV en `resultados/`:

```
python comparar_resultados.py
```

Muestra la tabla comparativa, verifica que ambas implementaciones generan la misma secuencia (columna *Misma secuencia*) y guarda `resultados/tabla_comparativa.csv`.

### 5.4 Ejemplo de resultados (semilla 42)

| N | π estimado | Error absoluto | Tiempo Python (ms) | Tiempo Java (ms) |
|---:|---:|---:|---:|---:|
| 1 000 | 3.312000 | 0.170407 | 2.224 | 1.245 |
| 10 000 | 3.137200 | 0.004393 | 23.149 | 1.209 |
| 100 000 | 3.142040 | 0.000447 | 196.578 | 8.494 |
| 1 000 000 | 3.143472 | 0.001879 | 2257.069 | 12.454 |

Los valores de π estimado, `Nc` y error son idénticos en Python y Java; los tiempos dependen del equipo y varían entre ejecuciones.

---

## 6. Estructura del proyecto

```
practica07_montecarlo/
├── python/
│   ├── main.py                        # Punto de entrada
│   ├── model/                         # MODELO
│   │   ├── lcg_random.py              #   Generador pseudoaleatorio (LCG 48 bits)
│   │   ├── monte_carlo_model.py       #   Lógica: π ≈ 4·Nc/N
│   │   └── resultado.py               #   Estructura de datos del resultado
│   ├── view/                          # VISTA
│   │   ├── console_view.py            #   Tabla en consola y exportación a CSV
│   │   └── plot_view.py               #   Gráficos con Matplotlib
│   └── controller/
│       └── experiment_controller.py   # CONTROLADOR: ejecuta y mide tiempos
├── java/src/
│   ├── Main.java                      # Punto de entrada
│   ├── model/                         # MODELO
│   │   ├── LcgRandom.java
│   │   ├── MonteCarloModel.java
│   │   └── Resultado.java
│   ├── view/
│   │   └── ConsoleView.java           # VISTA
│   └── controller/
│       └── ExperimentController.java  # CONTROLADOR
├── comparar_resultados.py             # Une los CSV y verifica la misma secuencia
└── resultados/                        # CSV y gráficos generados
```

---

## 7. Información adicional

### Cómo se logra la misma secuencia en Python y Java

El generador es un congruencial lineal de 48 bits (el mismo algoritmo de `java.util.Random`), implementado de forma idéntica en `lcg_random.py` y `LcgRandom.java`:

```
X(n+1) = (0x5DEECE66D · X(n) + 0xB) mod 2^48
```

Con la misma semilla, ambos programas obtienen el mismo `Nc` y el mismo π estimado. Si se usara el generador por defecto de cada lenguaje (Mersenne Twister en Python), las secuencias serían distintas.

### Funcionalidades
- Estimación de π para cuatro tamaños de muestra.
- Registro de π estimado, `Nc`, error absoluto y tiempo de ejecución.
- Exportación a CSV y tabla comparativa Python vs. Java.
- Gráficos: puntos dentro/fuera del círculo y error frente a N (con referencia 1/√N).

### Observaciones sobre los resultados
- El error disminuye en promedio como 1/√N, pero **no de forma monótona** en una sola ejecución: con N = 1 000 000 el error (0.001879) fue mayor que con N = 100 000 (0.000447).
- Java fue más rápido en todos los tamaños de muestra; la diferencia crece con N.
- Cada tamaño se ejecutó una vez con una sola semilla; para conclusiones más sólidas conviene repetir con varias semillas y promediar.

### Problemas comunes
- **`Falta un archivo...` al comparar:** aún no se ejecutó Python o Java, o el CSV de Java quedó en otra carpeta (ver 5.2).
- **`ModuleNotFoundError` en Python:** ejecute `main.py` desde dentro de la carpeta `python/`.
- **Aparece `?` en lugar de π en la consola de Windows:** es solo la codificación de la terminal; ejecute `chcp 65001` antes de correr Java. No afecta los cálculos ni los CSV.
- **La columna *Misma secuencia* dice `NO`:** se usaron semillas distintas en cada programa.

### Licencia y autoría
Proyecto académico de uso educativo.
**Autor:** [Nombre del estudiante] · **Docente:** José O. Guamán Q.
