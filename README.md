# 🐍 Suite de Ejemplos Prácticos en Python: 12 Librerías Fundamentales

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completado-success.svg)
![Architecture](https://img.shields.io/badge/Architecture-Modular-orange.svg)

Repositorio profesional con implementaciones completas, ejecutables y desacopladas de **12 librerías esenciales del ecosistema Python**, abarcando desde utilidades integradas en la biblioteca estándar hasta bibliotecas avanzadas de ciencia de datos, visualización, reportes PDF, APIs web y Machine Learning.

---

## 📁 Estructura del Repositorio

```text
Practica 1 Unidad 2/
├── .gitignore               # Configuración de exclusión para venv, cachés y artefactos
├── README.md                # Documentación exhaustiva del proyecto y guía de ejecución
├── requirements.txt         # Especificación de dependencias externas
├── practica 1.py            # Orquestador y menú interactivo de la suite
└── examples/
    ├── 01_math.py           # Librería math (Operaciones científicas, trigonometría)
    ├── 02_random.py         # Librería random (Muestreos, aleatoriedad, simulación)
    ├── 03_datetime.py       # Librería datetime (Zonas horarias, deltas y formatos)
    ├── 04_csv.py            # Librería csv (Procesamiento con reader, writer, DictReader)
    ├── 05_fpdf.py           # Librería fpdf2 (Reporte PDF con estilos y tablas)
    ├── 06_reportlab.py      # Librería reportlab (PDF con Platypus y Canvas dinámico)
    ├── 07_numpy.py          # Librería numpy (Arrays multidimensionales, álgebra lineal)
    ├── 08_pandas.py         # Librería pandas (DataFrames, limpieza, agregaciones)
    ├── 09_matplotlib.py     # Librería matplotlib (Dashboard gráfico en PNG 300 DPI)
    ├── 10_requests.py       # Librería requests (Cliente REST API, GET/POST, JSON)
    ├── 11_flask.py          # Librería flask (Microservicio RESTful con filtros)
    ├── 12_sklearn.py        # Librería scikit-learn (Machine learning supervisado)
    └── output/              # Directorio donde se generan los reportes y gráficas
```

---

## ⚙️ Requisitos e Instalación

### 1. Clonar el Repositorio o Situarse en la Carpeta Raíz
Abre tu terminal favorita (PowerShell, CMD, Bash o Zsh) en el directorio del proyecto:
```bash
cd "Practica 1 Unidad 2"
```

### 2. Creación y Activación del Entorno Virtual (Recomendado)
Es una buena práctica de ingeniería aislar las dependencias del proyecto:

- **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
  *(Si PowerShell restringe la ejecución de scripts, ejecuta primero `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`).*

- **En Windows (Símbolo del sistema / CMD):**
  ```cmd
  python -m venv venv
  venv\Scripts\activate.bat
  ```

- **En Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalación de Dependencias Externas
Instala las librerías requeridas mediante `pip`:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Las librerías integradas (`math`, `random`, `datetime`, `csv`) no requieren instalación adicional ya que forman parte de la biblioteca estándar de Python.

---

## 📚 Descripción Detallada de los 12 Ejemplos

| # | Archivo | Librería | Tipo | Conceptos Clave Demostrados |
|---|---|---|---|---|
| **01** | `01_math.py` | `math` | Estándar | Constantes ($\pi, e, \tau$), trigonometría, hipotenusa, redondeos (`ceil`, `floor`), logaritmos, combinatoria (`factorial`, `comb`, `gcd`) y distancia euclidiana 3D. |
| **02** | `02_random.py` | `random` | Estándar | Pseudoaleatoriedad, distribuciones uniformes, selecciones con y sin reemplazo (`choice`, `sample`, `choices` con pesos), `shuffle`, semillas y simulación de 10,000 tiros de dados. |
| **03** | `03_datetime.py` | `datetime` | Estándar | Manejo de zonas horarias (`timezone.utc`), parseo de fechas (`strptime`), formateo legible (`strftime`), aritmética con `timedelta` y auditoría de vencimiento de facturas. |
| **04** | `04_csv.py` | `csv` | Estándar | Lectura/escritura tabular con `csv.writer` y `csv.reader`, procesamiento estructurado con cabeceras mediante `csv.DictWriter` y `csv.DictReader`, y agregación salarial. |
| **05** | `05_fpdf.py` | `fpdf2` | Externa | Arquitectura orientada a objetos para PDFs (`header`, `footer`), márgenes, multiceldas para párrafos, diseño de cajas KPI y tablas corporativas con alternancia de color. |
| **06** | `06_reportlab.py` | `reportlab` | Externa | Motor de flujo Platypus (`SimpleDocTemplate`, `Paragraph`, `Spacer`, `Table`), Canvas personalizado con numeración de 2 pasadas ("Página X de Y") y estilos de párrafo editoriales. |
| **07** | `07_numpy.py` | `numpy` | Externa | Arrays $N$-dimensionales, máscaras booleanas, indexación vectorial, broadcasting, álgebra lineal (`linalg.inv`, `linalg.det`, `linalg.solve`) y normalización Z-Score. |
| **08** | `08_pandas.py` | `pandas` | Externa | Estructuras `DataFrame`, diagnóstico (`info`, `describe`), imputación de valores nulos (`fillna`, `median`), cálculo de columnas derivadas, agrupaciones `groupby` y exportación. |
| **09** | `09_matplotlib.py` | `matplotlib` | Externa | Backend `Agg` para entornos sin monitor, panel multipanel (3 columnas): serie temporal con marcadores, gráfico de barras con etiquetas y dispersión con mapas de color viridis a 300 DPI. |
| **10** | `10_requests.py` | `requests` | Externa | Peticiones HTTP GET y POST hacia la API REST JSONPlaceholder, query parameters, serialización JSON automática, headers personalizados y captura de excepciones (`HTTPError`, `Timeout`). |
| **11** | `11_flask.py` | `flask` | Externa | API RESTful con Flask: ruta de documentación (`/`), endpoint de catálogo (`/api/v1/products`) con filtrado por categoría y precio, ruta por ID y manejador de error 404 en JSON. |
| **12** | `12_sklearn.py` | `scikit-learn` | Externa | Flujo completo de Machine Learning supervisado: partición `train_test_split`, escalado Z-score (`StandardScaler`), regresión lineal vs árbol de decisión, métricas $R^2$, MAE, RMSE y predicción. |

---

## 🚀 Guía de Ejecución Paso a Paso

### Opción A: Usando el Menú Interactivo / Orquestador
Puedes iniciar el lanzador interactivo ejecutando:
```bash
python "practica 1.py"
```
Se desplegará una interfaz de consola donde puedes seleccionar el número del ejemplo deseado (1 al 12), ingresar `A` para ejecutar toda la suite de forma secuencial, o `0` para salir.

También puedes pasar el número de módulo como argumento directo:
```bash
python "practica 1.py" 7
```

---

### Opción B: Ejecución Individual de Cada Script

#### 1. Librería `math`
```bash
python examples/01_math.py
```
> **Salida esperada:** Cálculos de funciones trigonométricas, aproximaciones, logaritmos y demostración de cálculo geométrico 3D en la consola.

#### 2. Librería `random`
```bash
python examples/02_random.py
```
> **Salida esperada:** Muestras aleatorias, contraseñas seguras y gráfica de barras en consola con la distribución de probabilidad de 10,000 tiradas de dados.

#### 3. Librería `datetime`
```bash
python examples/03_datetime.py
```
> **Salida esperada:** Marcas temporales locales y UTC, conversión de formatos de fecha, cálculo de días restantes y reporte de facturas vencidas o vigentes.

#### 4. Librería `csv`
```bash
python examples/04_csv.py
```
> **Salida esperada:** Creación y lectura de `examples/output/inventario_productos.csv` y `examples/output/nomina_empleados.csv`, con cálculo de métricas financieras.

#### 5. Librería `fpdf2`
```bash
python examples/05_fpdf.py
```
> **Salida esperada:** Generación del documento PDF `examples/output/reporte_ejecutivo_fpdf.pdf` con membretes, KPI y tabla de desempeño.

#### 6. Librería `reportlab`
```bash
python examples/06_reportlab.py
```
> **Salida esperada:** Compilación del documento `examples/output/reporte_estructurado_reportlab.pdf` con motor de flujo Platypus y Canvas dinámico.

#### 7. Librería `numpy`
```bash
python examples/07_numpy.py
```
> **Salida esperada:** Creación de tensores, demostración de broadcasting sobre matrices de precios, solución de sistema lineal $Ax = b$ y normalización Z-Score.

#### 8. Librería `pandas`
```bash
python examples/08_pandas.py
```
> **Salida esperada:** Resumen de diagnóstico de datos, imputación de nulos, agregaciones `groupby` por región y exportación de `examples/output/resumen_ventas_pandas.csv`.

#### 9. Librería `matplotlib`
```bash
python examples/09_matplotlib.py
```
> **Salida esperada:** Creación de la imagen en alta definición `examples/output/dashboard_metricas_matplotlib.png` con 3 paneles gráficos (líneas, barras y dispersión).

#### 10. Librería `requests`
```bash
python examples/10_requests.py
```
> **Salida esperada:** Solicitudes HTTP a JSONPlaceholder, procesamiento de respuestas JSON, creación de recurso mediante POST y captura controlada de error 404.

#### 11. Librería `flask`
```bash
python examples/11_flask.py
```
> **Salida esperada:** Inicio del servidor de desarrollo en `http://127.0.0.1:5000`. Puedes probar las siguientes rutas desde el navegador o con `curl`:
> - Documentación base: `http://127.0.0.1:5000/`
> - Catálogo completo: `http://127.0.0.1:5000/api/v1/products`
> - Filtrar por categoría: `http://127.0.0.1:5000/api/v1/products?categoria=Perifericos`
> - Filtrar por precio: `http://127.0.0.1:5000/api/v1/products?max_precio=200`
> - Producto específico: `http://127.0.0.1:5000/api/v1/products/1`
> *(Presiona `Ctrl + C` en la terminal para finalizar la ejecución de Flask).*

#### 12. Librería `scikit-learn`
```bash
python examples/12_sklearn.py
```
> **Salida esperada:** Entrenamiento de modelos de Regresión Lineal y Árbol de Decisión, reporte de métricas ($R^2$, MAE, RMSE) y estimación de precios para 3 inmuebles nuevos.

---

## 📤 Instrucciones para Subir el Proyecto a GitHub

Sigue estos comandos en tu terminal para publicar el repositorio en tu cuenta de GitHub:

```bash
# 1. Inicializar el repositorio Git local
git init

# 2. Configurar la rama principal como 'main'
git branch -M main

# 3. Comprobar los archivos rastreados (verificando que .gitignore funcione)
git status

# 4. Agregar todos los archivos al área de preparación (staging)
git add .

# 5. Realizar el commit inicial
git commit -m "feat: suite completa con ejemplos practicos de 12 librerias fundamentales en Python"

# 6. Vincular el repositorio local con tu repositorio remoto en GitHub
# (Reemplaza <TU_USUARIO> y <TU_REPOSITORIO> con tus datos reales)
git remote add origin https://github.com/<TU_USUARIO>/<TU_REPOSITORIO>.git

# 7. Subir el código a GitHub
git push -u origin main
```

---

## 🛠️ Buenas Prácticas Aplicadas

1. **Rutas Independientes del Sistema Operativo:** Empleo riguroso de `pathlib.Path` para garantizar compatibilidad total en Windows, macOS y Linux.
2. **Backend No Interactivo en Visualización:** Uso de `matplotlib.use('Agg')` para permitir la exportación de gráficos en servidores headless o entornos CI/CD sin interfaz gráfica de usuario.
3. **Manejo Defensivo de Excepciones:** Bloques `try/except` específicos (`HTTPError`, `Timeout`, `RequestException`) en consumo de APIs externas.
4. **Clean Code & Tipado Semántico:** Docstrings informativos, nombres de funciones autoexplicativos y organización modular siguiendo la guía de estilo PEP 8.
5. **Aislamiento de Salidas:** Los scripts generan sus artefactos (PDF, CSV, PNG) en una carpeta dedicada `output/`, protegida en `.gitignore` para no contaminar el historial de Git.
