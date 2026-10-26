# Simulación SIR (Java + NetLogo)

Simulación estocástica de la propagación de una enfermedad con el modelo epidemiológico **SIR** (Susceptibles, Infectados, Recuperados), implementada en Java con arquitectura MVC. Los resultados se exportan a CSV para compararlos con una versión equivalente en NetLogo.

## 1. Descripción del proyecto

**Propósito:** simular, paso a paso, cómo una enfermedad se propaga en una población y cómo evolucionan los tres grupos del modelo:

- **S** (Susceptibles): personas que pueden contagiarse.
- **I** (Infectados): personas que están contagiadas y pueden contagiar.
- **R** (Recuperados): personas que ya se recuperaron y no vuelven a contagiarse.

**Problema que resuelve:** permite observar cómo cambian las curvas S, I y R al variar parámetros como los infectados iniciales o la tasa de infección, y validar el resultado comparando la implementación en Java con la de NetLogo.

## 2. Tecnologías utilizadas

| Herramienta | Uso |
|---|---|
| Java (JDK 8 o superior) | Lógica de la simulación y exportación de resultados |
| Patrón MVC | Organización del código en modelo, vista y controlador |
| CSV | Formato de salida de los resultados |
| NetLogo | Modelo equivalente para la comparación visual de curvas |

## 3. Instalación

1. Instala un **JDK 8 o superior** y verifica que esté disponible:

   ```bash
   java -version
   javac -version
   ```

2. Descarga o clona el proyecto y entra a la carpeta:

   ```bash
   cd simulacion-sir
   ```

3. Compila el código fuente (genera los `.class` en `out/`):

   ```bash
   javac -d out src/main/java/Main.java src/main/java/*/*.java
   ```

No se necesitan librerías externas ni gestor de dependencias.

## 4. Uso

Ejecuta la simulación desde la carpeta `simulacion-sir`:

```bash
java -cp out Main
```

Al terminar, se muestra el progreso en consola y se crea el archivo **`resultados_java.csv`** en la carpeta desde la que ejecutaste el comando.

Formato del CSV (un registro por paso, del 0 al 100):

```csv
tiempo,susceptibles,infectados,recuperados
0,95,5,0
1,...
```

## 5. Configuración

Los parámetros del escenario se cambian en `src/main/java/Main.java`:

```java
int poblacionTotal = 100;
int infectadosIniciales = 5;   // Infectados iniciales
double beta = 0.30;            // Tasa de infección
double gamma = 0.10;           // Tasa de recuperación
int pasosSimulacion = 100;
```

> **Importante:** después de modificar los valores hay que **volver a compilar** (paso 3 de Instalación). De lo contrario se seguirá ejecutando con los `.class` anteriores.

### Cómo interpretar `beta`

En `ModeloSIR`, `beta` se evalúa **por cada pareja infectado-susceptible** en cada paso. Por eso, la probabilidad real de que un susceptible se contagie es `1 - (1 - beta)^I`, donde `I` es el número de infectados.

| Escenario | Parámetros | Comportamiento esperado |
|---|---|---|
| Base | `I0 = 5`, `beta = 0.30`, `gamma = 0.10` | Brote muy rápido, pico en los primeros pasos |
| Brote extremo | `I0 = 20`, `beta = 0.50`, `gamma = 0.10` | Casi toda la población se infecta en el paso 1 |
| Curva gradual | `I0 = 2`, `beta = 0.002`, `gamma = 0.10` | Crecimiento progresivo con pico visible hacia el paso 20-30 |

Con `beta` menor a ~0.001 (población de 100) el brote se apaga sin propagarse.

## 6. Estructura del proyecto

```
simulacion-sir/
├── src/main/java/
│   ├── Main.java                         # Punto de entrada y parámetros
│   ├── controller/
│   │   └── ControladorSimulacion.java    # Coordina la simulación y guarda el CSV
│   ├── model/
│   │   ├── ModeloSIR.java                # Lógica de contagio y recuperación
│   │   ├── Individuo.java                # Persona con su estado
│   │   ├── Estado.java                   # SUSCEPTIBLE, INFECTADO, RECUPERADO
│   │   └── Resultado.java                # Conteo S/I/R de un paso (fila del CSV)
│   └── view/
│       └── VistaConsola.java             # Mensajes en consola
├── out/                                  # Clases compiladas (.class)
├── capturas/                             # Capturas de pantalla
└── informe/                              # Informe del trabajo
```

## 7. Información adicional

### Funcionamiento del modelo

En cada paso (tick) se evalúa a todos los individuos según el estado del paso anterior:

1. **Contagio:** cada susceptible puede infectarse con probabilidad `beta` frente a cada infectado.
2. **Recuperación:** cada infectado se recupera con probabilidad `gamma`.

Como el modelo es **estocástico**, los resultados varían ligeramente en cada ejecución, aunque la forma general de las curvas se mantiene.

### Comparación con NetLogo

El archivo `resultados_java.csv` se carga en el modelo de NetLogo (botón **Cargar Java**) para graficar y comparar las curvas de susceptibles, infectados y recuperados contra la simulación nativa de NetLogo. Para que la comparación sea válida, los parámetros deben ser **los mismos en ambos programas**.

### Licencia

Proyecto académico. Define aquí la licencia que corresponda.
