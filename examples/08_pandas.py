"""
Ejemplo 08: Análisis y Manipulación de Datos con 'Pandas'
=========================================================
Construcción de DataFrames, inspección exploratoria, limpieza de valores nulos,
filtrado condicional, transformaciones vectorizadas, agregaciones groupby y exportación.
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def crear_dataframe_muestra() -> pd.DataFrame:
    print("\n" + "=" * 50)
    print(" 1. CREACIÓN DEL DATAFRAME INICIAL (CON VALORES NULOS)")
    print("=" * 50)
    datos = {
        "transaccion_id": [101, 102, 103, 104, 105, 106, 107, 108],
        "fecha": [
            "2026-01-10", "2026-01-11", "2026-01-12", "2026-01-12",
            "2026-01-14", "2026-01-15", "2026-01-16", "2026-01-16",
        ],
        "cliente": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Heidi"],
        "region": ["Norte", "Sur", "Norte", "Este", "Sur", "Norte", np.nan, "Este"],
        "unidades": [5, 2, np.nan, 10, 1, 4, 7, 3],
        "precio_unitario": [120.0, 85.5, 300.0, 45.0, 210.0, 95.0, 150.0, 80.0],
        "descuento": [0.10, 0.0, 0.05, 0.15, np.nan, 0.0, 0.20, 0.05],
    }
    df = pd.DataFrame(datos)
    print(df)
    return df


def exploracion_de_datos(df: pd.DataFrame):
    print("\n" + "=" * 50)
    print(" 2. EXPLORACIÓN Y DIAGNÓSTICO DE LA ESTRUCTURA")
    print("=" * 50)
    print(f"Dimensiones del DataFrame (filas, columnas): {df.shape}")
    print("\nTipos de datos por columna:")
    print(df.dtypes)

    print("\nConteo de valores nulos o faltantes (NaN):")
    print(df.isna().sum())

    print("\nEstadísticas descriptivas de variables numéricas:")
    print(df.describe().round(2))


def limpieza_de_datos(df: pd.DataFrame) -> pd.DataFrame:
    print("\n" + "=" * 50)
    print(" 3. LIMPIEZA DE DATOS (Data Cleaning & Imputation)")
    print("=" * 50)
    df_limpio = df.copy()

    # 1. Conversión de fecha a formato datetime nativo
    df_limpio["fecha"] = pd.to_datetime(df_limpio["fecha"])

    # 2. Imputación de nulos en variables categóricas
    df_limpio["region"] = df_limpio["region"].fillna("No Especificada")

    # 3. Imputación en variables numéricas con la mediana
    mediana_unidades = df_limpio["unidades"].median()
    df_limpio["unidades"] = df_limpio["unidades"].fillna(mediana_unidades).astype(int)

    # 4. Relleno de descuento nulo con 0.0
    df_limpio["descuento"] = df_limpio["descuento"].fillna(0.0)

    print("✓ Valores nulos tratados correctamente:")
    print(df_limpio)
    return df_limpio


def transformacion_y_filtrado(df: pd.DataFrame) -> pd.DataFrame:
    print("\n" + "=" * 50)
    print(" 4. INGENIERÍA DE CARACTERÍSTICAS Y FILTRADO")
    print("=" * 50)
    # Cálculo de ingresos brutos y netos
    df["subtotal"] = df["unidades"] * df["precio_unitario"]
    df["monto_descuento"] = df["subtotal"] * df["descuento"]
    df["total_neto"] = df["subtotal"] - df["monto_descuento"]

    print("Columnas calculadas añadidas (subtotal, total_neto):")
    print(df[["cliente", "unidades", "precio_unitario", "descuento", "total_neto"]])

    # Filtro condicional complejo: Región 'Norte' con total_neto superior a $400
    filtro = (df["region"] == "Norte") & (df["total_neto"] > 400.0)
    ventas_destacadas = df.loc[filtro, ["transaccion_id", "cliente", "region", "total_neto"]]
    print(f"\nTransacciones en Región Norte con Venta > $400:\n{ventas_destacadas}")

    return df


def agregaciones_y_reporte(df: pd.DataFrame, ruta_exportacion: Path):
    print("\n" + "=" * 50)
    print(" 5. AGREGACIONES (groupby) Y PIVOT TABLES")
    print("=" * 50)
    # Resumen agrupado por Región
    resumen_region = (
        df.groupby("region")
        .agg(
            num_transacciones=("transaccion_id", "count"),
            unidades_totales=("unidades", "sum"),
            ingreso_total=("total_neto", "sum"),
            ticket_promedio=("total_neto", "mean"),
        )
        .round(2)
        .sort_values(by="ingreso_total", ascending=False)
    )

    print("Resumen agrupado por Región:")
    print(resumen_region)

    # Exportación del reporte a CSV
    resumen_region.to_csv(ruta_exportacion, index=True, encoding="utf-8")
    print(f"\n✓ Reporte analítico exportado a: {ruta_exportacion}")


def main():
    print("DEMOSTRACIÓN COMPLETA DE LA LIBRERÍA 'pandas'")
    df_raw = crear_dataframe_muestra()
    exploracion_de_datos(df_raw)
    df_clean = limpieza_de_datos(df_raw)
    df_transformed = transformacion_y_filtrado(df_clean)

    archivo_salida = OUTPUT_DIR / "resumen_ventas_pandas.csv"
    agregaciones_y_reporte(df_transformed, archivo_salida)

    print("\n" + "=" * 50)
    print("✓ Fin de la demostración de 'pandas'")
    print("=" * 50)


if __name__ == "__main__":
    main()
