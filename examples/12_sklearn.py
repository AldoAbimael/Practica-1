"""
Ejemplo 12: Machine Learning con 'scikit-learn'
===============================================
Flujo completo de aprendizaje supervisado para regresión:
- Preparación y estructuración de dataset (Predicción de Valor Inmobiliario)
- Partición de datos en conjuntos de Entrenamiento y Prueba (train_test_split)
- Escalado y normalización de variables con StandardScaler
- Entrenamiento y ajuste de modelos (Regresión Lineal y Árbol de Decisión)
- Evaluación de métricas cuantitativas: R² Score, MAE, RMSE
- Predicción e inferencia sobre nuevas observaciones no vistas
"""

import sys
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def generar_dataset_inmobiliario(n_muestras: int = 150):
    """
    Genera un dataset sintético controlado con variables explicativas realistas:
    X1: Superficie construida (m²) [50 a 250]
    X2: Número de habitaciones [1 a 5]
    X3: Distancia al centro financiero (km) [1 a 25]
    y: Precio de la vivienda en miles de USD ($K)
    """
    np.random.seed(42)
    m2 = np.random.uniform(50, 250, size=n_muestras)
    habitaciones = np.random.randint(1, 6, size=n_muestras)
    distancia_centro = np.random.uniform(1, 25, size=n_muestras)

    # Ecuación generadora subyacente con ruido estocástico
    # Precio base: $50K + ($1.8K x m2) + ($15K x habitacion) - ($3.5K x distancia_km) + error
    ruido = np.random.normal(0, 15, size=n_muestras)
    precios = 50.0 + (1.8 * m2) + (15.0 * habitaciones) - (3.5 * distancia_centro) + ruido

    matriz_x = np.column_stack([m2, habitaciones, distancia_centro])
    vector_y = precios
    return matriz_x, vector_y


def main():
    print("=" * 60)
    print(" DEMOSTRACIÓN DE MACHINE LEARNING CON 'scikit-learn'")
    print("=" * 60)

    # 1. Carga y partición del conjunto de datos
    X, y = generar_dataset_inmobiliario(200)
    print(f"Total de observaciones generadas: {X.shape[0]}")
    print(f"Variables explicativas (Features): [Superficie m², Habitaciones, Distancia Centro km]")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )
    print(f"Muestras de entrenamiento (75%): {X_train.shape[0]}")
    print(f"Muestras de evaluación (25%)   : {X_test.shape[0]}")

    # 2. Escalado de características (Normalización Z-score)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 3. Entrenamiento del Modelo 1: Regresión Lineal
    print("\n" + "-" * 50)
    print(" 1. REGRESIÓN LINEAL (LinearRegression)")
    print("-" * 50)
    modelo_lr = LinearRegression()
    modelo_lr.fit(X_train_scaled, y_train)

    predicciones_lr = modelo_lr.predict(X_test_scaled)
    r2_lr = r2_score(y_test, predicciones_lr)
    mae_lr = mean_absolute_error(y_test, predicciones_lr)
    rmse_lr = np.sqrt(mean_squared_error(y_test, predicciones_lr))

    print(f"R² Score (Coeficiente Determinación): {r2_lr:.4f} (Explicación del {r2_lr*100:.2f}% de la varianza)")
    print(f"Error Absoluto Medio (MAE)           : ${mae_lr:.2f}K USD")
    print(f"Raíz de Error Cuadrático Medio (RMSE): ${rmse_lr:.2f}K USD")

    # 4. Entrenamiento del Modelo 2: Árbol de Decisión
    print("\n" + "-" * 50)
    print(" 2. ÁRBOL DE DECISIÓN (DecisionTreeRegressor)")
    print("-" * 50)
    modelo_dt = DecisionTreeRegressor(max_depth=5, random_state=42)
    modelo_dt.fit(X_train, y_train)  # Los árboles no requieren escalado obligatorio

    predicciones_dt = modelo_dt.predict(X_test)
    r2_dt = r2_score(y_test, predicciones_dt)
    mae_dt = mean_absolute_error(y_test, predicciones_dt)
    rmse_dt = np.sqrt(mean_squared_error(y_test, predicciones_dt))

    print(f"R² Score (Árbol de Decisión)        : {r2_dt:.4f}")
    print(f"Error Absoluto Medio (MAE)          : ${mae_dt:.2f}K USD")
    print(f"Raíz de Error Cuadrático Medio (RMSE): ${rmse_dt:.2f}K USD")

    # 5. Inferencia con nuevos casos de prueba
    print("\n" + "-" * 50)
    print(" 3. INFERENCIA Y PREDICCIÓN CON NUEVOS INMUEBLES")
    print("-" * 50)
    nuevas_casas = np.array([
        [120.0, 3, 5.0],   # Casa A: 120m², 3 hab, 5km del centro
        [210.0, 4, 15.0],  # Casa B: 210m², 4 hab, 15km del centro
        [65.0, 1, 2.0],    # Depto C: 65m², 1 hab, 2km del centro
    ])

    nuevas_casas_scaled = scaler.transform(nuevas_casas)
    pred_precios = modelo_lr.predict(nuevas_casas_scaled)

    etiquetas = ["Casa Familiar A", "Residencia B", "Apartamento C"]
    for i in range(len(nuevas_casas)):
        sup, hab, dist = nuevas_casas[i]
        print(f"Propiedad: {etiquetas[i]}")
        print(f"  Características : {sup} m² | {int(hab)} habitaciones | {dist} km al centro")
        print(f"  Precio Estimado : ${pred_precios[i]:,.2f}K USD (${pred_precios[i]*1000:,.0f} USD)")
        print()

    print("=" * 60)
    print("✓ Fin de la demostración de 'scikit-learn'")
    print("=" * 60)


if __name__ == "__main__":
    main()
