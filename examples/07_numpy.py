"""
Ejemplo 07: Computación Científica con 'NumPy'
==============================================
Demostración de matrices multidimensionales (ndarrays), indexación booleana,
broadcasting vectorial, operaciones de álgebra lineal y análisis estadístico.
"""

import sys
import numpy as np

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def demostrar_creacion_y_atributos():
    print("\n" + "=" * 50)
    print(" 1. CREACIÓN E INSPECCIÓN DE ARRAYS MULTIDIMENSIONALES")
    print("=" * 50)
    vector_1d = np.array([10, 20, 30, 40, 50], dtype=np.int32)
    matriz_2d = np.array([[1.5, 2.8, 3.2], [4.1, 5.9, 6.4]], dtype=np.float64)
    tensor_3d = np.zeros((2, 3, 4))  # 2 bloques, 3 filas, 4 columnas
    secuencia_espaciada = np.linspace(0, 10, num=5)
    matriz_identidad = np.eye(3)

    print(f"Vector 1D              : {vector_1d} | Shape: {vector_1d.shape} | Dim: {vector_1d.ndim}")
    print(f"Matriz 2D:\n{matriz_2d}")
    print(f"  - Shape: {matriz_2d.shape} | Tipo: {matriz_2d.dtype} | Tamaño: {matriz_2d.size} elementos")
    print(f"Tensor 3D (zeros) shape: {tensor_3d.shape}")
    print(f"Linspace (0 a 10 en 5) : {secuencia_espaciada}")
    print(f"Matriz Identidad 3x3:\n{matriz_identidad}")


def demostrar_indexacion_y_mascaras():
    print("\n" + "=" * 50)
    print(" 2. SLICING AVANZADO Y MÁSCARAS BOOLEANAS")
    print("=" * 50)
    datos = np.arange(10, 100, 10).reshape(3, 3)
    print(f"Matriz 3x3 original:\n{datos}")

    # Slicing: Filas 0 y 1, Columnas 1 y 2
    submatriz = datos[0:2, 1:3]
    print(f"\nSubmatriz [0:2, 1:3]:\n{submatriz}")

    # Máscara Booleana
    mascara = datos > 50
    print(f"\nMáscara booleana (elemento > 50):\n{mascara}")
    print(f"Valores filtrados que cumplen la condición: {datos[mascara]}")

    # np.where para reemplazo condicional
    clasificados = np.where(datos >= 50, "ALTO", "BAJO")
    print(f"\nTransformación con np.where (>=50 ? ALTO : BAJO):\n{clasificados}")


def demostrar_broadcasting():
    print("\n" + "=" * 50)
    print(" 3. BROADCASTING Y OPERACIONES VECTORIZADAS")
    print("=" * 50)
    precios_base = np.array([[100, 200, 300], [400, 500, 600]])  # Shape (2, 3)
    impuesto_por_columna = np.array([1.16, 1.08, 1.21])  # Shape (3,)

    # Se propaga la fila unidimensional sobre cada fila de la matriz 2D
    precios_con_impuesto = precios_base * impuesto_por_columna
    print(f"Precios base (2x3):\n{precios_base}")
    print(f"Factores de impuesto (1x3): {impuesto_por_columna}")
    print(f"Precios calculados con Broadcasting:\n{precios_con_impuesto.round(2)}")


def demostrar_algebra_lineal():
    print("\n" + "=" * 50)
    print(" 4. ÁLGEBRA LINEAL (numpy.linalg)")
    print("=" * 50)
    # Matriz de coeficientes A y vector de resultados B
    # Sistema:
    # 2x + 3y = 8
    # 1x + 4y = 9
    matriz_a = np.array([[2.0, 3.0], [1.0, 4.0]])
    vector_b = np.array([8.0, 9.0])

    det_a = np.linalg.det(matriz_a)
    inversa_a = np.linalg.inv(matriz_a)
    solucion_x = np.linalg.solve(matriz_a, vector_b)

    print(f"Matriz de coeficientes A:\n{matriz_a}")
    print(f"Determinante de A       : {det_a:.4f}")
    print(f"Matriz Inversa A⁻¹:\n{inversa_a}")
    print(f"Vector b                : {vector_b}")
    print(f"Solución del sistema Ax=b: x = {solucion_x[0]:.2f}, y = {solucion_x[1]:.2f}")

    # Producto punto matricial (@)
    verificacion = matriz_a @ solucion_x
    print(f"Verificación (A @ x)    : {verificacion} (debe coincidir con b)")


def demostrar_estadisticas_y_normalizacion():
    print("\n" + "=" * 50)
    print(" 5. ESTADÍSTICAS Y CASO PRÁCTICO DE NORMALIZACIÓN")
    print("=" * 50)
    np.random.seed(42)
    calificaciones = np.random.randint(50, 100, size=(5, 3))  # 5 alumnos, 3 materias

    print(f"Matriz de calificaciones (5 alumnos x 3 materias):\n{calificaciones}")
    print(f"Promedio general        : {np.mean(calificaciones):.2f}")
    print(f"Desviación estándar     : {np.std(calificaciones):.2f}")
    print(f"Promedio por materia    : {np.mean(calificaciones, axis=0).round(2)}")
    print(f"Promedio por alumno     : {np.mean(calificaciones, axis=1).round(2)}")
    print(f"Calificación más alta   : {np.max(calificaciones)} (Índice plano: {np.argmax(calificaciones)})")

    # Estandarización Z-Score: (X - media) / desviacion_estandar
    media_materias = np.mean(calificaciones, axis=0)
    std_materias = np.std(calificaciones, axis=0)
    z_score = (calificaciones - media_materias) / std_materias

    print(f"\nCalificaciones Estandarizadas (Z-Score):\n{z_score.round(3)}")


def main():
    print("DEMOSTRACIÓN COMPLETA DE LA LIBRERÍA 'numpy'")
    demostrar_creacion_y_atributos()
    demostrar_indexacion_y_mascaras()
    demostrar_broadcasting()
    demostrar_algebra_lineal()
    demostrar_estadisticas_y_normalizacion()
    print("\n" + "=" * 50)
    print("✓ Fin de la demostración de 'numpy'")
    print("=" * 50)


if __name__ == "__main__":
    main()
