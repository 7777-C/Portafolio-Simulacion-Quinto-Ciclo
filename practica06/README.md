# Práctica 06 – Validación estadística de números pseudoaleatorios (LCG, Chi-cuadrado y KS)

Dos implementaciones equivalentes con arquitectura **Modelo – Vista – Controlador**.

```
python/                          java/
  main.py                          src/Main.java
  comparar.py                      src/modelo/        GeneradorLCG, FuncionesEspeciales,
  modelo/       lcg.py, ...                           PruebasEstadisticas, MonteCarloPi
  vista/        vista_consola.py   src/vista/         VistaConsola
  controlador/  controlador.py     src/controlador/   Controlador
```

## Ejecución

**Python** (requiere matplotlib solo para los gráficos):
```
cd python
python main.py
```

**Java** (JDK 17+; el PNG se genera con Java2D, sin dependencias):
```
cd java
mkdir out
javac -encoding UTF-8 -d out src/Main.java src/modelo/*.java src/vista/*.java src/controlador/*.java
java -cp out Main
```
(En Windows PowerShell usa `src\modelo\*.java`, etc. Si ves mal las tildes: `java -Dstdout.encoding=UTF-8 -cp out Main`.)

**Tabla comparativa Python vs Java** (tras ejecutar ambos): `cd python && python comparar.py`

## Qué hace
- LCG: X(n+1) = (a·Xn + c) mod m, U = X/m. Config. principal: semilla 12345, a=1664525, c=1013904223, m=2^32.
- Chi-cuadrado: k=10 intervalos, gl=9, α=0.05.
- Kolmogorov-Smirnov: D = max(D+, D-), F(x)=x.
- Comparación de 5 configuraciones (NumRecipes, ANSI C, RANDU, periodo corto, degenerado).
- Estimación de π por Monte Carlo (pares consecutivos del LCG) para N = 1 000 … 1 000 000.
- Los valores p se calculan con el mismo método numérico en ambos lenguajes (gamma incompleta y serie de Kolmogorov), sin librerías externas.
- Salidas en `salida/`: gráficos PNG y `resultados_*.csv`.
