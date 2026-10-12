## 1. Descripción del Proyecto

Este proyecto implementa un **modelo matemático** para estimar la posibilidad de lluvia a lo largo de 24 horas, aplicando la fórmula:

$$
I = 0.5H + 0.3N + 0.2T_f
$$

Donde:

- **H** = humedad normalizada (0 a 1).
- **N** = nubosidad normalizada (0 a 1).
- **Tf** = factor de temperatura (según tabla del PDF).
- **I** = índice de posibilidad de lluvia.

### Propósito

Comprender el proceso de construcción de un modelo matemático y analizar su comportamiento mediante Python, aplicando buenas prácticas de diseño.

### Problema que resuelve

Permite **identificar en qué horas del día existe posibilidad de lluvia** a partir de datos de humedad, nubosidad y temperatura, clasificando cada hora en 4 estados:

| Índice I | Estado |
|---|---|
| I < 0.40 | Sin lluvia |
| 0.40 ≤ I < 0.60 | Baja posibilidad |
| 0.60 ≤ I < 0.75 | Lluvia probable |
| I ≥ 0.75 | Lluvia |

La práctica corresponde a la **Unidad 1: Introducción a la Simulación** de la asignatura **Simulación – Ciclo 5**.

---

## 2. Tecnologías Utilizadas

| Tecnología | Versión | Uso |
|---|---|---|
| Python | 3.11 o superior | Lenguaje principal |
| NumPy | ≥ 1.26 | Cálculo numérico y eje X de la gráfica |
| Matplotlib | ≥ 3.8 | Generación de la gráfica |
| ABC (`abc`) | estándar | Clases abstractas para Strategy |
| Visual Studio Code | última | Entorno de desarrollo |
| Git / GitHub | — | Control de versiones |
| Oracle Linux | — | Sistema operativo |

**Arquitectura:** Modelo–Vista–Controlador (MVC) + Strategy.

---

## 3. Instalación

### Requisitos previos

- Python 3.11 o superior.
- Git (opcional, para clonar el repositorio).
- Sistema operativo: Linux, Windows o macOS.

### Paso 1 – Clonar o descargar el proyecto

```bash
git clone https://github.com/7777-C/Portafolio-Simulacion-Quinto-Ciclo.git
cd Portafolio-Simulacion-Quinto-Ciclo
```

O simplemente descomprimir el `.zip` en la ubicación deseada.

### Paso 2 – Crear el entorno virtual

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**

```powershell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```

### Paso 3 – Instalar dependencias

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Contenido de `requirements.txt`:

```text
numpy
matplotlib
```

---

## 4. Uso

### Ejecución principal

Desde la **raíz del proyecto** (donde está `main.py`):

```bash
python main.py
```

### ¿Qué hace el programa?

1. Carga los datos del PDF desde `datos/datos_entrada.py`.
2. Calcula el **factor de temperatura Tf** con interpolación lineal.
3. Calcula el **índice I** para cada hora.
4. Clasifica cada hora en 4 estados.
5. Muestra una **tabla** por consola.
6. Genera una **gráfica** en `grafica_lluvia.png`.

### Salidas generadas

```text
modelo_lluvia/
├── grafica_lluvia.png
└── (tabla impresa en consola)
```

### Personalizar parámetros

Edita el archivo `datos/datos_entrada.py`:

```python
class DatosEntrada:
    HORAS       = ["06:00", "08:00", "10:00", "12:00", "14:00",
                   "16:00", "18:00", "20:00", "22:00"]
    HUMEDAD     = [65, 70, 68, 60, 75, 85, 92, 88, 80]
    NUBOSIDAD   = [40, 50, 45, 30, 70, 85, 95, 90, 75]
    TEMPERATURA = [14, 16, 18, 22, 20, 18, 16, 17, 15]
```

---

## 5. Estructura del Proyecto

```text
modelo_lluvia/
│
├── main.py                          # Punto de entrada
├── requirements.txt
├── README.md
│
├── modelo/                          # MODELO – lógica matemática
│   ├── __init__.py
│   ├── estrategias.py               # Strategy: Tf y clasificación
│   └── modelo_lluvia.py             # Cálculo del índice I
│
├── vista/                           # VISTA – presentación
│   ├── __init__.py
│   └── vista_lluvia.py              # Tabla + gráfica
│
├── controlador/                     # CONTROLADOR – orquesta M + V
│   ├── __init__.py
│   └── controlador_lluvia.py
│
├── datos/                           # DATOS de entrada
│   ├── __init__.py
│   └── datos_entrada.py
│
└── grafica_lluvia.png               # Generada al ejecutar
```

### Descripción de carpetas

| **Carpeta** | **Responsabilidad** |
| :--- | :--- |
| `modelo/` | Fórmula `I = 0.5H + 0.3N + 0.2Tf`, cálculo de Tf y clasificación |
| `vista/` | Tabla en consola y gráfica con Matplotlib |
| `controlador/` | Coordina el Modelo y la Vista |
| `datos/` | Datos crudos del PDF |

---

## 6. Modelos Matemáticos Implementados

### 6.1 Fórmula principal

$$
I = 0.5H + 0.3N + 0.2T_f
$$

### 6.2 Factor de temperatura (Tf)

| **Temperatura** | **Tf** |
| :--- | :--- |
| ≤ 10 °C | 1.00 |
| 12 °C | 0.90 |
| 14 °C | 0.80 |
| 16 °C | 0.70 |
| 18 °C | 0.60 |
| 20 °C | 0.50 |
| 22 °C | 0.40 |
| 24 °C | 0.30 |
| 26 °C | 0.20 |
| ≥ 28 °C | 0.10 |

### 6.3 Interpolación lineal (obligatoria)

El PDF solo da Tf para temperaturas pares, pero la tabla de datos incluye **15 °C** y **17 °C**. Por eso se interpola:

$$
T_f = v_1 + (v_2-v_1)\frac{t-t_1}{t_2-t_1}
$$

**Ejemplos:**

- 17 °C → `Tf = 0.70 + (0.60 - 0.70) × (17 - 16) / (18 - 16) = 0.65`
- 15 °C → `Tf = 0.80 + (0.70 - 0.80) × (15 - 14) / (16 - 14) = 0.75`

### 6.4 Clasificación

| **Índice I** | **Estado** |
| :--- | :--- |
| I < 0.40 | Sin lluvia |
| 0.40 ≤ I < 0.60 | Baja posibilidad |
| 0.60 ≤ I < 0.75 | Lluvia probable |
| I ≥ 0.75 | Lluvia |

---

## 7. Información Adicional

### 7.1 Interpretación de las gráficas

- **Eje X:** horas del día (06:00 a 22:00).
- **Eje Y:** índice I (0 a 1).
- **Línea azul:** valor del índice I en cada hora.
- **Puntos de colores:** estado según la clasificación.
  - 🟢 Verde → Sin lluvia.
  - 🟡 Amarillo → Baja posibilidad.
  - 🟠 Naranja → Lluvia probable.
  - 🔴 Rojo → Lluvia.
- **Líneas punteadas:** umbrales 0.40, 0.60 y 0.75.

**Comportamiento observado:**

- El índice **crece** desde las 06:00 hasta las 18:00 (pico máximo: 0.885).
- Luego **decrece** ligeramente hacia las 22:00.
- Las horas con mayor probabilidad de lluvia son **16:00, 18:00, 20:00 y 22:00**.

### 7.2 Notas y consideraciones

- La **interpolación lineal** es necesaria para 15 °C y 17 °C.
- Los **pesos** (0.5, 0.3, 0.2) suman 1.0, garantizando que I esté entre 0 y 1.
- La **humedad** es la variable de mayor peso en el modelo.
- El uso del backend `Agg` en Matplotlib evita errores en Linux sin entorno gráfico.

### 7.3 Declaración de uso de Inteligencia Artificial

Durante el desarrollo de esta práctica se utilizó **inteligencia artificial como apoyo puntual**, únicamente en los siguientes aspectos:

- **Aclaración de conceptos** que no se tenían del todo claros (por ejemplo, en qué consiste el patrón Strategy y cómo se diferencia de la herencia tradicional).
- **Explicación de la sintaxis y uso de librerías** específicas de Python (NumPy, Matplotlib) en fragmentos donde no se sabía cómo proceder.
- **Apoyo en la interpretación de las gráficas**, ya que en un inicio no se comprendía qué significaban los puntos de colores ni cómo se relacionaban con los umbrales.

**No se utilizó la IA** para generar el proyecto completo, la arquitectura MVC, los algoritmos de cálculo ni la lógica interna de cada clase. Todo el diseño, la organización de carpetas, la implementación de las ecuaciones y las decisiones técnicas fueron realizados por el autor de esta práctica.

El uso de esta herramienta se declara bajo el principio de **transparencia y honestidad académica** establecido en el resultado de aprendizaje de la unidad.
