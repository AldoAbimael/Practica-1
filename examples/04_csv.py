"""
Ejemplo 04: Librería Estándar 'csv'
===================================
Operaciones de lectura y escritura de archivos planos CSV usando:
- csv.writer y csv.reader (enfoque basado en listas de valores)
- csv.DictWriter y csv.DictReader (enfoque estructurado basado en diccionarios y cabeceras)
"""

import csv
import sys
from pathlib import Path

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


# Directorio de salida seguro para los artefactos generados
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def escribir_csv_con_writer(ruta_archivo: Path):
    print("\n" + "=" * 50)
    print(" 1. ESCRITURA CON csv.writer (Listas de datos)")
    print("=" * 50)
    filas = [
        ["ID", "Producto", "Categoria", "Precio", "Stock"],
        [101, "Teclado Mecánico", "Periféricos", 85.50, 40],
        [102, "Monitor 4K 27p", "Monitores", 349.99, 15],
        [103, "Mouse Inalámbrico", "Periféricos", 29.90, 80],
        [104, "Silla Ergonómica", "Mobiliario", 199.00, 10],
    ]

    with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerows(filas)

    print(f"✓ Archivo escrito exitosamente en: {ruta_archivo.name}")


def leer_csv_con_reader(ruta_archivo: Path):
    print("\n" + "=" * 50)
    print(" 2. LECTURA CON csv.reader (Secuencial fila a fila)")
    print("=" * 50)
    with open(ruta_archivo, mode="r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        encabezados = next(lector)
        print(f"Encabezados detectados: {encabezados}")
        print("-" * 50)
        for num_fila, fila in enumerate(lector, start=1):
            id_prod, nombre, categoria, precio, stock = fila
            print(f"Fila {num_fila}: [{id_prod}] {nombre:<18} | {categoria:<12} | ${float(precio):>6.2f} | Stock: {stock}")


def escribir_csv_con_dictwriter(ruta_archivo: Path):
    print("\n" + "=" * 50)
    print(" 3. ESCRITURA CON csv.DictWriter (Estructuras de Diccionario)")
    print("=" * 50)
    campos = ["id_empleado", "nombre", "departamento", "salario_mensual"]
    empleados = [
        {"id_empleado": "EMP-01", "nombre": "Laura Méndez", "departamento": "Ingeniería", "salario_mensual": 4500.00},
        {"id_empleado": "EMP-02", "nombre": "Carlos Gómez", "departamento": "Marketing", "salario_mensual": 3200.00},
        {"id_empleado": "EMP-03", "nombre": "Diana Ross", "departamento": "Ingeniería", "salario_mensual": 4900.00},
        {"id_empleado": "EMP-04", "nombre": "Roberto Silva", "departamento": "Finanzas", "salario_mensual": 3800.00},
    ]

    with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(empleados)

    print(f"✓ Archivo estructurado con encabezados guardado en: {ruta_archivo.name}")


def procesar_csv_con_dictreader(ruta_archivo: Path):
    print("\n" + "=" * 50)
    print(" 4. ANÁLISIS Y AGREGACIÓN CON csv.DictReader")
    print("=" * 50)
    salarios_por_depto = {}
    total_nomina = 0.0
    conteo_empleados = 0

    with open(ruta_archivo, mode="r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            depto = fila["departamento"]
            salario = float(fila["salario_mensual"])
            total_nomina += salario
            conteo_empleados += 1
            salarios_por_depto.setdefault(depto, []).append(salario)

    print(f"Total de empleados analizados : {conteo_empleados}")
    print(f"Nómina mensual total          : ${total_nomina:,.2f}")
    promedio_general = total_nomina / conteo_empleados if conteo_empleados else 0
    print(f"Salario promedio general      : ${promedio_general:,.2f}")

    print("\nPromedio por Departamento:")
    for depto, sueldos in salarios_por_depto.items():
        media_depto = sum(sueldos) / len(sueldos)
        print(f"  - {depto:<15}: ${media_depto:,.2f} ({len(sueldos)} colaboradores)")


def main():
    print("DEMOSTRACIÓN COMPLETA DE LA LIBRERÍA 'csv'")
    archivo_productos = OUTPUT_DIR / "inventario_productos.csv"
    archivo_empleados = OUTPUT_DIR / "nomina_empleados.csv"

    escribir_csv_con_writer(archivo_productos)
    leer_csv_con_reader(archivo_productos)
    escribir_csv_con_dictwriter(archivo_empleados)
    procesar_csv_con_dictreader(archivo_empleados)

    print("\n" + "=" * 50)
    print(f"✓ Archivos CSV generados en la carpeta: {OUTPUT_DIR}")
    print("=" * 50)


if __name__ == "__main__":
    main()
