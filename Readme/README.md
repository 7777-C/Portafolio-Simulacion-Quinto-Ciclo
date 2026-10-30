# Generador Congruencial Lineal (LCG) - Arquitectura MVC

## 1. Descripción del proyecto
### Propósito
Este proyecto implementa el **Generador Congruencial Lineal (LCG)** para la generación de números pseudoaleatorios, estructurado bajo el patrón de diseño **Modelo-Vista-Controlador (MVC)** tanto en **Java** como en **Python**.

### Problema Resuelto
Permite la simulación, análisis tabular y visualización gráfica de secuencias pseudoaleatorias mediante la formulación matemática:
$$X_{n+1} = (a \cdot X_n + c) \pmod m$$
Garantizando el manejo correcto de desbordamientos de enteros (overflow) y la normalización de datos al intervalo $[0, 1)$.

---

## 2. Tecnologías utilizadas
* **Lenguajes de Programación:** Java (JDK 11+) y Python 3.11+.
* **Librerías de Python:** `matplotlib` (para generación de gráficos).
* **Entorno de Ejecución:** Terminal / PowerShell / Command Prompt.
* **Patrón de Arquitectura:** Model-View-Controller (MVC).

---

## 3. Instalación
Para preparar el entorno de trabajo y ejecutar el proyecto, sigue los siguientes pasos:

### Prerrequisitos
* Tener instalado Java JDK 11 o superior.
* Tener instalado Python 3.8 o superior.

### Instalación de dependencias en Python
Abre la terminal en la raíz del proyecto y ejecuta:

```bash
cd lcg_project_python
pip install -r requirements.txt
```

---

## 4. Uso y Ejecución

### Ejecución del módulo en Java
1. Abre la terminal y navega hasta la carpeta `src` del proyecto Java:
   ```powershell
   cd lcg_project_java\src
   ```
2. Compila las clases:
   ```powershell
   javac ecu\edu\unl\lcg\Main.java ecu\edu\unl\lcg\model\LcgModel.java ecu\edu\unl\lcg\view\LcgView.java ecu\edu\unl\lcg\controller\LcgController.java
   ```
3. Ejecuta el programa:
   ```powershell
   java ecu.edu.unl.lcg.Main
   ```

### Ejecución del módulo en Python
1. Navega a la carpeta de Python desde la terminal:
   ```powershell
   cd lcg_project_python
   ```
2. Ejecuta el script principal:
   ```powershell
   python main.py
   ```

---

## 5. Configuración
Los parámetros predeterminados de la fórmula LCG están definidos en los modelos de ambos lenguajes según el estándar de Knuth:
* **Multiplicador ($a$):** $1\,664\,525$
* **Incremento ($c$):** $1\,013\,904\,223$
* **Módulo ($m$):** $2^{32} = 4\,294\,967\,296$
* **Semilla inicial ($X_0$):** $12\,345$

Para modificar la semilla o la cantidad de iteraciones, ajusta la instancia de instanciación del modelo dentro de los archivos `Main.java` o `main.py`.

---

## 6. Estructura del proyecto

```text
proyecto_lcg_mvc/
│
├── lcg_project_java/                # Módulo Java
│   └── src/
│       └── ecu/edu/unl/lcg/
│           ├── model/              # LcgModel.java (Lógica matemática LCG)
│           ├── view/               # LcgView.java (Formateo de tablas en consola)
│           ├── controller/         # LcgController.java (Coordinador)
│           └── Main.java           # Punto de entrada
│
└── lcg_project_python/              # Módulo Python
    ├── models/                      # lcg_model.py (Lógica LCG)
    ├── views/                       # lcg_view.py (Visualización con matplotlib)
    ├── controllers/                 # lcg_controller.py (Coordinador)
    ├── config.py                    # Constantes globales
    ├── main.py                      # Punto de entrada
    └── requirements.txt             # Archivo de dependencias
```

---

## 7. Información adicional
* **Exportación de Gráficas:** La ejecución en Python genera y guarda automáticamente la imagen `grafica_lcg.png` en la carpeta `lcg_project_python/`.
* **Validación de Resultados:** Ambos módulos aplican precisión flotante estricta para garantizar que el valor normalizado $U_i = \frac{X_i}{m}$ se mantenga idéntico en las ejecuciones de Java y Python.