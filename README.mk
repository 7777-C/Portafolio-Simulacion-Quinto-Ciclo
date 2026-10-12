## 1. Descripción del Proyecto

Este proyecto implementa y compara **cuatro paradigmas de simulación** aplicados a un mismo
sistema de estudio: el **crecimiento poblacional**.

### Propósito

Diferenciar, mediante modelos computacionales, el comportamiento de:

- **Modelo Determinístico** – crecimiento exponencial continuo, sin aleatoriedad.
- **Modelo Discreto** – crecimiento por intervalos de tiempo enteros.
- **Modelo Estocástico** – incorpora ruido aleatorio con distribución normal.
- **Modelo Continuo (Euler)** – aproximación numérica de la ecuación diferencial.

### Problema que resuelve

Permite **visualizar y comparar** cómo cambia una población bajo distintos supuestos
matemáticos, y analizar el efecto de la **tasa de crecimiento (r)**, el **nivel de ruido (σ)**
y el **tamaño de paso (Δt)** sobre los resultados.

La práctica corresponde a la **Unidad 1: Introducción a la Simulación** de la asignatura
**Simulación – Ciclo 5**.

---

## 2. Tecnologías Utilizadas

| Tecnología | Versión | Uso |
|---|---|---|
| Python | 3.11 o superior | Lenguaje principal |
| NumPy | ≥ 1.26 | Cálculo numérico y generación de ruido |
| Pandas | ≥ 2.0 | Tabla comparativa y exportación CSV |
| Matplotlib | ≥ 3.8 | Gráficas comparativas e individuales |
| SciPy | ≥ 1.11 | Soporte estadístico (base para extensiones) |
| Visual Studio Code | última | Entorno de desarrollo |
| Git / GitHub | — | Control de versiones |

**Arquitectura:** Modelo–Vista–Controlador (MVC).

---

## 3. Instalación

### Requisitos previos

- Python 3.11 o superior (recomendado 3.11 o 3.12).
- Git (opcional, para clonar el repositorio).
- Sistema operativo: Windows, Linux o macOS.

### Paso 1 – Clonar o descargar el proyecto

```bash
git clone <URL_DEL_REPOSITORIO>
cd comparacion_modelos
````


O simplemente descomprimir el `.zip` en la ubicación deseada.

### Paso 2 – Crear el entorno virtual

**Windows (PowerShell):**

```
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```


**Linux / macOS:**

```
python3 -m venv venv
source venv/bin/activate
```


### Paso 3 – Instalar dependencias

```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```


Contenido de `requirements.txt`:

```
numpy
pandas
matplotlib
scipy
```


---

## 4. Uso

### Ejecución principal

Desde la **raíz del proyecto** (donde está `main.py`):

```
python main.py
```


### ¿Qué hace el programa?

1. Ejecuta los 4 modelos con los parámetros definidos en `config/parametros.py`.
2. Muestra por consola los **valores finales** de cada modelo.
3. Genera 4 **gráficas individuales** (una por modelo).
4. Genera 1 **gráfica comparativa** con los 4 modelos superpuestos.
5. Exporta la **tabla comparativa** a `outputs/resultados.csv`.

### Salidas generadas

```
outputs/
├── figuras/
│   ├── comparativa.png
│   ├── deterministico.png
│   ├── discreto.png
│   ├── estocastico.png
│   └── continuo_euler.png
└── resultados.csv
```


### Personalizar parámetros

Edita el archivo `config/parametros.py`:

```
DATOS_ENTRADA = [1000, 1100, 1250, 1400, 1600, 1850, 2100]
P0     = DATOS_ENTRADA[0]   # Población inicial
R      = 0.15               # Tasa de crecimiento
SIGMA  = 50                 # Nivel de ruido (modelo estocástico)
TIEMPO = 20                 # Tiempo total de simulación
DT     = 0.1                # Paso para Euler
SEMILLA = 42                # Semilla para reproducibilidad
```


---

## 5. Estructura del Proyecto

```
comparacion_modelos/
│
├── main.py                   
├── requirements.txt
├── README.md
│
├── config/                     
│   ├── __init__.py
│   └── parametros.py
│
├── models/                      # MODELO 
│   ├── __init__.py
│   ├── base_model.py            # Clase abstracta
│   ├── deterministico.py        # P(t) = P0 * e^(r*t)
│   ├── discreto.py              # P(t+1) = P(t) + r*P(t)
│   ├── estocastico.py           # P(t+1) = P(t) + r*P(t) + ε
│   └── continuo_euler.py        # Euler: P(t+dt) = P(t) + dt*r*P(t)
│
├── views/                       # VISTA
│   ├── __init__.py
│   ├── grafica_comparativa.py
│   ├── grafica_individual.py
│   └── tabla_resultados.py
│
├── controllers/                 # CONTROLADOR
│   ├── __init__.py
│   └── simulacion_controller.py
│
└── outputs/                     
    ├── figuras/
    └── resultados.csv
```


### Descripción de carpetas

| **Carpeta**    | **Responsabilidad**                                           |
| :------------- | :------------------------------------------------------------ |
| `config/`      | Parámetros de entrada: `P0`, `r`, `σ`, `dt`, tiempo, semilla. |
| `models/`      | Cada paradigma de simulación en su propio archivo.            |
| `views/`       | Generación de gráficas y tablas con Pandas/Matplotlib.        |
| `controllers/` | Coordina los modelos y las vistas.                            |
| `outputs/`     | Figuras PNG y archivo CSV exportados.                         |

---

## 6. Modelos Matemáticos Implementados

### 6.1 Determinístico

$$\nP(t) = P_0 e^{rt}\n$$

### 6.2 Discreto

$$\nP_{t+1} = P_t + rP_t\n$$

### 6.3 Estocástico

$$\nP_{t+1} = P_t + rP_t + \varepsilon_t, \quad \varepsilon_t \sim N(0, \sigma^2)\n$$

### 6.4 Continuo (Euler)

$$\n\frac{dP}{dt} = rP \quad \Rightarrow \quad P_{t+\Delta t} = P_t + \Delta t(rP_t)\n$$

---

## 7. Información Adicional

### 7.1 Interpretación de las gráficas

- **Determinístico vs. Continuo (Euler):** ambas curvas deben ser casi idénticas; si se alejan, hay que reducir `dt` para mejorar la aproximación.
- **Discreto vs. Determinístico:** el modelo discreto siempre queda ligeramente por debajo del continuo porque la capitalización se hace en pasos enteros.
- **Estocástico:** se dispersa alrededor del determinístico. A mayor `σ`, mayor dispersión.
- **Efecto de** `r`**:** si `r > 0` la población crece; si `r = 0` se mantiene constante; si `r < 0` decrece.
- **Efecto de** `σ`**:** con `σ = 0` el modelo estocástico coincide con el discreto.

### 7.2 Notas y consideraciones

- El modelo estocástico **nunca produce poblaciones negativas** (se aplica `max(p, 0)`).
- El modelo continuo se aproxima con Euler; su precisión depende de `dt`.
- La semilla fija (`SEMILLA = 42`) garantiza resultados **reproducibles** en el modelo estocástico.

### 7.3 Declaración de uso de Inteligencia Artificial

Durante el desarrollo de esta práctica se utilizó **inteligencia artificial como apoyo**
**puntual**, únicamente en los siguientes aspectos:

- **Aclaración de conceptos** que no se tenían del todo claros.
- **Explicación de la sintaxis y uso de librerías** específicas de Python (NumPy, Matplotlib)
  en fragmentos donde no se sabía cómo proceder.
- **Apoyo en la interpretación de las gráficas**, ya que en un inicio no se comprendía por qué
  las curvas se separaban ni qué significaba la dispersión del modelo estocástico.

**No se utilizó la IA** para generar el proyecto completo, la arquitectura MVC, los algoritmos
de simulación ni la lógica interna de cada modelo. Todo el diseño, la organización de carpetas,
la implementación de las ecuaciones y las decisiones técnicas fueron realizados por el autor
de esta práctica.

El uso de esta herramienta se declara bajo el principio de **transparencia y honestidad**
**académica** establecido en el resultado de aprendizaje de la unidad.

### 7.4 Referencias

- Diapositivas de la Semana 2 – Asignatura Simulación.
- NumPy Documentation: [https://numpy.org/doc/](https://numpy.org/doc/)
- Pandas Documentation: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
- Matplotlib Documentation: [https://matplotlib.org/stable/](https://matplotlib.org/stable/)
- SciPy Documentation: [https://docs.scipy.org/](https://docs.scipy.org/)

---

## 8. Autor y Datos Académicos

| **Campo**           | **Detalle**                      |
| :------------------ | :------------------------------- |
| Asignatura          | Simulación                       |
| Ciclo               | 5                                |
| Unidad              | U1: Introducción a la Simulación |
| Práctica            | Nro. 02                          |
| Docente             | José O. Guamán Q.                |
| Director de Carrera | Edison L. Coronel Romero         |
| Fecha               | Octubre 2026                     |

---