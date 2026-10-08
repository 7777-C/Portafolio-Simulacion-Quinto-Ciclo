# Modelo de Simulación de Posibilidad de Lluvia

**Asignatura:** Simulación
**Ciclo:** 5to
**Práctica Nro.:** 01
**Título:** Construcción y simulación computacional de un modelo matemático
**Autor:** Mark González
**Docente:** Ing. José Guamán
**Fecha:** 05 de Octubre del 2026

---

## 1. Descripción

Este proyecto implementa un **modelo matemático para estimar la posibilidad de lluvia** a lo largo de un período de 24 horas.

El cálculo se realiza mediante la siguiente fórmula:

$$
I = 0.5H + 0.3N + 0.2T_f
$$

Donde:

* **H** = Humedad normalizada, con valores entre 0 y 1.
* **N** = Nubosidad normalizada, con valores entre 0 y 1.
* **Tf** = Factor de temperatura, determinado mediante una tabla de valores.
* **I** = Índice de posibilidad de lluvia.

El resultado obtenido se clasifica de acuerdo con las siguientes reglas:

| Índice `I`        | Estado           |
| ----------------- | ---------------- |
| `I < 0.40`        | Sin lluvia       |
| `0.40 ≤ I < 0.60` | Baja posibilidad |
| `0.60 ≤ I < 0.75` | Lluvia probable  |
| `I ≥ 0.75`        | Lluvia           |

---

## 2. Arquitectura del proyecto

Para organizar el sistema se aplicaron dos patrones de diseño:

### 2.1 Patrón MVC

Se utiliza el patrón **Modelo - Vista - Controlador ** para separar las responsabilidades principales de la aplicación.

| Componente      | Responsabilidad                                                          |
| --------------- | ------------------------------------------------------------------------ |
| **Modelo**      | Contiene la lógica de negocio y realiza el cálculo del índice de lluvia. |
| **Vista**       | Presenta los resultados mediante una tabla y una gráfica.                |
| **Controlador** | Coordina la comunicación entre los datos, el modelo y la vista.          |


### 2.2 Patrón Strategy

El patrón **Strategy** se utiliza dentro del modelo para permitir diferentes estrategias de cálculo.

En este proyecto se aplica principalmente para:

* Determinar el **factor de temperatura `Tf`**.
* Clasificar el **índice de posibilidad de lluvia**.

---

## 3. Estructura del proyecto

```text
modelo_lluvia/
│
├── modelo/
│   ├── __init__.py
│   ├── estrategias.py
│   └── modelo_lluvia.py
│
├── vista/
│   ├── __init__.py
│   └── vista_lluvia.py
│
├── controlador/
│   ├── __init__.py
│   └── controlador_lluvia.py
│
├── datos/
│   ├── __init__.py
│   └── datos_entrada.py
│
├── main.py
├── grafica_lluvia.png
└── README.md
```

### Descripción de los archivos

| Archivo                 | Descripción                                                          |
| ----------------------- | -------------------------------------------------------------------- |
| `main.py`               | Punto de entrada de la aplicación.                                   |
| `modelo_lluvia.py`      | Contiene la lógica principal del modelo matemático.                  |
| `estrategias.py`        | Implementa las estrategias relacionadas con `Tf` y la clasificación. |
| `vista_lluvia.py`       | Muestra los resultados y genera la gráfica.                          |
| `controlador_lluvia.py` | Coordina el funcionamiento general de la aplicación.                 |
| `datos_entrada.py`      | Contiene los datos utilizados para la simulación.                    |
| `grafica_lluvia.png`    | Gráfica generada a partir de los resultados.                         |
| `README.md`             | Documentación del proyecto.                                          |

---

## 4. Interpolación del factor de temperatura `Tf`

La tabla para el modelo define valores de `Tf`:

```text
10, 12, 14, 16, 18, 20, 22, 24, 26, 28 °C
```

Sin embargo, los datos utilizados en la simulación contienen temperaturas que no aparecen directamente en dicha tabla, como:

```text
15 °C
17 °C
```

Para obtener un valor de `Tf` para estas temperaturas se implementó **interpolación lineal**.

La fórmula utilizada es:

$$
Tf = Tf_1 + (Tf_2-Tf_1)
\frac{T-T_1}{T_2-T_1}
$$

### Ejemplo: 17 °C

Si:

```text
T1 = 16 °C
Tf1 = 0.70

T2 = 18 °C
Tf2 = 0.60
```

Entonces:

$$
Tf = 0.70 + (0.60-0.70)
\frac{17-16}{18-16}
$$

$$
Tf = 0.70 - 0.05
$$

$$
Tf = 0.65
$$

Por lo tanto:

```text
17 °C → Tf = 0.65
```

### Ejemplo: 15 °C

Utilizando los valores correspondientes a 14 °C y 16 °C:

```text
14 °C → Tf = 0.80
16 °C → Tf = 0.70
```

Se obtiene:

$$
Tf = 0.80 + (0.70-0.80)
\frac{15-14}{16-14}
$$

$$
Tf = 0.75
$$

Por lo tanto:

```text
15 °C → Tf = 0.75
```
---

## 5. Funcionamiento del modelo

El proceso general de la simulación es:

```text
Datos de entrada
       │
       ▼
Normalización de H y N
       │
       ▼
Cálculo de Tf
       │
       ▼
Cálculo del índice I
       │
       ▼
Clasificación del resultado
       │
       ▼
Presentación en tabla
       │
       ▼
Generación de gráfica
```

El índice se obtiene mediante:

$$
I = 0.5H + 0.3N + 0.2T_f
$$

---

## 6. Tecnologías utilizadas

* **Python 3**
* **NumPy**
* **Matplotlib**
* Patrón **MVC**
* Patrón **Strategy**
* Interpolación lineal
* Modelado matemático
* Simulación computacional

---

## ▶7. Cómo ejecutar el proyecto

### 7.1 Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

Ingresar a la carpeta:

```bash
cd modelo_lluvia
```

### 7.2 Crear un entorno virtual

```bash
python -m venv venv
```

### 7.3 Activar el entorno virtual

En Windows:

```powershell
venv\Scripts\activate
```

En Linux/macOS:

```bash
source venv/bin/activate
```

### 7.4 Instalar las dependencias

```bash
pip install numpy matplotlib
```

### 7.5 Ejecutar el programa

```bash
python main.py
```

---

## 8. Salida esperada

Al ejecutar el programa se muestran los resultados.

Además, se genera una gráfica:

```text
grafica_lluvia.png
```
---

## 9. Resultados

|  Hora | Humedad | Nubosidad | Temp. |    H |    N |   Tf | Índice | Estado           |
| :---: | ------: | --------: | ----: | ---: | ---: | ---: | -----: | ---------------- |
| 06:00 |      65 |        40 |    14 | 0.65 | 0.40 | 0.80 |  0.605 | Lluvia probable  |
| 08:00 |      70 |        50 |    16 | 0.70 | 0.50 | 0.70 |  0.640 | Lluvia probable  |
| 10:00 |      68 |        45 |    18 | 0.68 | 0.45 | 0.60 |  0.595 | Baja posibilidad |
| 12:00 |      60 |        30 |    22 | 0.60 | 0.30 | 0.40 |  0.470 | Baja posibilidad |
| 14:00 |      75 |        70 |    20 | 0.75 | 0.70 | 0.50 |  0.685 | Lluvia probable  |
| 16:00 |      85 |        85 |    18 | 0.85 | 0.85 | 0.60 |  0.800 | Lluvia           |
| 18:00 |      92 |        95 |    16 | 0.92 | 0.95 | 0.70 |  0.885 | Lluvia           |
| 20:00 |      88 |        90 |    17 | 0.88 | 0.90 | 0.65 |  0.840 | Lluvia           |
| 22:00 |      80 |        75 |    15 | 0.80 | 0.75 | 0.75 |  0.775 | Lluvia           |

### Interpretación

El valor máximo del índice se presenta a las **18:00**, con:

```text
I = 0.885
```

De acuerdo con las reglas establecidas, este resultado corresponde al estado:

**Lluvia**

Las horas con mayor índice de posibilidad de lluvia son:

* **16:00 → I = 0.800**
* **18:00 → I = 0.885**
* **20:00 → I = 0.840**
* **22:00 → I = 0.775**

---

## 10. Declaración de uso de Inteligencia Artificial

En cumplimiento de los principios de **transparencia, honestidad y responsabilidad académica**, se declara el uso de herramientas de Inteligencia Artificial durante el desarrollo del proyecto.

### 10.1 ¿Se utilizó IA?

**Sí, de forma limitada y como apoyo conceptual.**

### 10.2 ¿Cómo se utilizó?

La Inteligencia Artificial fue utilizada como herramienta de consulta y explicación para:

* Comprender conceptos relacionados con el patrón de diseño **Strategy**.
* Diferenciar un patrón de diseño de una estructura convencional de carpetas.
* Obtener orientación conceptual sobre la organización **MVC**.
* Comprender mensajes de error de Python y posibles causas.
* Comprender el procedimiento matemático de la **interpolación lineal**.
* Resolver dudas puntuales relacionadas con la implementación del modelo.

### 10.3 ¿Qué tanto se utilizó?

El uso de IA se limitó a la etapa de **comprensión, consulta y orientación conceptual** y no sustituyó el trabajo de implementación realizado en el proyecto.

### 10.4 ¿Se utilizó IA para generar el código?

La IA fue utilizada como apoyo para comprender conceptos y resolver dudas, pero las clases, métodos y lógica fueron desarrollados y revisados por el autor.

### 10.5 ¿Qué se aprendió del proceso?

El uso de IA como herramienta de aprendizaje permiti reforzar los siguientes conocimientos:

* Diferencia entre **arquitectura y patrones de diseño**.
* Organización de un proyecto utilizando **MVC**.
* Aplicación del patrón **Strategy**.
* Utilización de **interpolación lineal**.
* Implementación de un modelo matemático mediante Python.
* Interpretación de los resultados de una simulación.
* Identificación y corrección de errores durante el desarrollo.

### 10.6 Declaración final

El autor declara que el proyecto fue desarrollado comprendiendo su funcionamiento y que puede explicar las principales decisiones tomadas durante su implementación.

La Inteligencia Artificial fue utilizada como una **herramienta de apoyo para el aprendizaje y la comprensión conceptual**, sin sustituir el proceso de desarrollo, prueba y validación del proyecto.

---

## 11. Referencias

* Material de clase y diapositivas de la semana 1 de la asignatura **Simulación**.
* **Guía de Actividades Práctico-Experimentales Nro. 001**.
* Python Software Foundation. *Python Documentation*.
* Matplotlib Development Team. *Matplotlib Documentation*.
* Refactoring.Guru. *Strategy Design Pattern*.

---

##  Autor

**Mark González**

Estudiante de Ingeniería en Sistemas

**Asignatura:** Simulacion
**Ciclo:** 5to
**Año:** 2026
