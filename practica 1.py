"""
Práctica 1 - Unidad 2: Suite Integral de 12 Librerías Fundamentales en Python
=============================================================================
Menú interactivo y orquestador para ejecutar y explorar cada uno de los
12 módulos prácticos desarrollados en el repositorio.
"""

import subprocess
import sys
from pathlib import Path

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


BASE_DIR = Path(__file__).resolve().parent
EXAMPLES_DIR = BASE_DIR / "examples"

MODULOS = [
    ("01_math.py", "Librería math (Constantes, trigonometría, redondeo, potencias)"),
    ("02_random.py", "Librería random (Números aleatorios, selecciones, shuffle, dados)"),
    ("03_datetime.py", "Librería datetime (Fechas, strftime/strptime, timedelta)"),
    ("04_csv.py", "Librería csv (Lectura y escritura con writer y DictReader)"),
    ("05_fpdf.py", "Librería fpdf2 (Generación de PDF estructurado y tablas)"),
    ("06_reportlab.py", "Librería reportlab (PDF con Platypus, Flowables y Canvas)"),
    ("07_numpy.py", "Librería numpy (Arrays multidimensionales, álgebra lineal, stats)"),
    ("08_pandas.py", "Librería pandas (DataFrames, limpieza, agrupaciones, exportación)"),
    ("09_matplotlib.py", "Librería matplotlib (Gráficos de líneas, barras y dispersión)"),
    ("10_requests.py", "Librería requests (Consumo de APIs REST, GET/POST, JSON)"),
    ("11_flask.py", "Librería flask (Microservicio API REST con rutas y filtros)"),
    ("12_sklearn.py", "Librería scikit-learn (Machine Learning: Regresión y predicción)"),
]


def ejecutar_script(nombre_script: str):
    ruta_script = EXAMPLES_DIR / nombre_script
    if not ruta_script.exists():
        print(f"\n[ERROR] No se encontró el archivo: {ruta_script}")
        return

    print("\n" + "=" * 70)
    print(f" EJECUTANDO: {nombre_script}")
    print("=" * 70)
    try:
        # Se ejecuta con el intérprete de Python en uso
        subprocess.run([sys.executable, str(ruta_script)], check=True)
    except subprocess.CalledProcessError as err:
        print(f"\n[ERROR] El script finalizó con código de salida: {err.returncode}")
    except KeyboardInterrupt:
        print("\n[INFO] Ejecución interrumpida por el usuario.")


def mostrar_menu():
    while True:
        print("\n" + "=" * 70)
        print("    SUITE DE EJEMPLOS EN PYTHON - PRÁCTICA 1 UNIDAD 2")
        print("=" * 70)
        for idx, (script, desc) in enumerate(MODULOS, start=1):
            print(f" [{idx:>2}] {desc}")
        print(" [ A] Ejecutar todos los scripts secuencialmente (excepto Flask)")
        print(" [ 0] Salir")
        print("-" * 70)

        opcion = input("Selecciona una opción (1-12, A, 0): ").strip().upper()

        if opcion == "0":
            print("\n¡Hasta luego!")
            break
        elif opcion == "A":
            for script, _ in MODULOS:
                if script == "11_flask.py":
                    print("\n[INFO] Omitiendo Flask en modo automático para evitar bloqueo del servidor.")
                    continue
                ejecutar_script(script)
        elif opcion.isdigit() and 1 <= int(opcion) <= len(MODULOS):
            script_seleccionado = MODULOS[int(opcion) - 1][0]
            ejecutar_script(script_seleccionado)
        else:
            print("\n[AVISO] Opción no válida. Por favor ingresa un número del 1 al 12, 'A' o '0'.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        param = sys.argv[1]
        if param.isdigit() and 1 <= int(param) <= len(MODULOS):
            ejecutar_script(MODULOS[int(param) - 1][0])
        else:
            print(f"[AVISO] Argumento inválido '{param}'. Usa un número del 1 al 12.")
    else:
        mostrar_menu()
