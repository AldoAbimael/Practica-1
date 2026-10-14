"""
Ejemplo 02: Librería Estándar 'random'
======================================
Demostración de generación de números pseudoaleatorios, selecciones probabilísticas,
mezclas en el lugar (shuffling), reproducibilidad por semilla y simulaciones prácticas (dados y cartas).
"""

import random
import string
import sys
from collections import Counter

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def demostrar_numeros_aleatorios():
    print("\n" + "=" * 50)
    print(" 1. GENERACIÓN DE NÚMEROS PSEUDOALEATORIOS")
    print("=" * 50)
    flotante_0_1 = random.random()
    flotante_rango = random.uniform(10.5, 25.0)
    entero_inclusivo = random.randint(1, 100)
    entero_pasos = random.randrange(0, 101, 10)

    print(f"random() [0.0, 1.0)          : {flotante_0_1:.6f}")
    print(f"uniform(10.5, 25.0)          : {flotante_rango:.4f}")
    print(f"randint(1, 100)              : {entero_inclusivo}")
    print(f"randrange(0, 101, paso=10)   : {entero_pasos}")


def demostrar_selecciones_y_mezclas():
    print("\n" + "=" * 50)
    print(" 2. SELECCIONES Y MEZCLAS EN COLECCIONES")
    print("=" * 50)
    lenguajes = ["Python", "JavaScript", "Rust", "Go", "Kotlin", "C++"]
    print(f"Colección original : {lenguajes}")

    # Selección simple
    seleccionado = random.choice(lenguajes)
    print(f"choice()           : {seleccionado}")

    # Selección sin reemplazo (sample)
    muestra_sin_rep = random.sample(lenguajes, k=3)
    print(f"sample(k=3)        : {muestra_sin_rep}")

    # Selección ponderada con pesos (choices)
    opciones = ["Común", "Raro", "Épico", "Legendario"]
    pesos = [70, 20, 8, 2]  # Probabilidades relativas
    loot_drop = random.choices(opciones, weights=pesos, k=5)
    print(f"choices() ponderado: {loot_drop}")

    # Mezcla en el lugar (inplace shuffle)
    copia_lenguajes = lenguajes.copy()
    random.shuffle(copia_lenguajes)
    print(f"shuffle() mezclar  : {copia_lenguajes}")


def demostrar_reproducibilidad():
    print("\n" + "=" * 50)
    print(" 3. CONTROL DE SEMILLA (REPRODUCIBILIDAD)")
    print("=" * 50)
    semilla = 42

    random.seed(semilla)
    secuencia_1 = [random.randint(1, 50) for _ in range(5)]

    random.seed(semilla)
    secuencia_2 = [random.randint(1, 50) for _ in range(5)]

    print(f"Semilla fijada en {semilla}")
    print(f"Secuencia intento A: {secuencia_1}")
    print(f"Secuencia intento B: {secuencia_2}")
    print(f"¿Son idénticas?    : {secuencia_1 == secuencia_2}")


def simulacion_lanzamiento_dados(n_lanzamientos: int = 10_000):
    print("\n" + "=" * 50)
    print(f" 4. SIMULACIÓN: {n_lanzamientos:,} LANZAMIENTOS DE 2 DADOS")
    print("=" * 50)
    resultados = [random.randint(1, 6) + random.randint(1, 6) for _ in range(n_lanzamientos)]
    conteo = Counter(resultados)

    print("Suma | Frecuencia | Porcentaje | Gráfica de distribución")
    print("-" * 55)
    for suma in range(2, 13):
        freq = conteo[suma]
        porcentaje = (freq / n_lanzamientos) * 100
        barra = "█" * int(porcentaje * 1.5)
        print(f" {suma:>2}  |  {freq:>6}   |   {porcentaje:>5.2f}%  | {barra}")


def caso_practico_generador_clave(longitud: int = 14) -> str:
    print("\n" + "=" * 50)
    print(" 5. CASO PRÁCTICO: GENERADOR DE CREDENCIALES SEGURAS")
    print("=" * 50)
    caracteres = string.ascii_letters + string.digits + "!@#$%&*-_=+"
    # Asegurar al menos uno de cada tipo
    clave_base = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%&*-_=+"),
    ]
    clave_restante = [random.choice(caracteres) for _ in range(longitud - 4)]
    password_list = clave_base + clave_restante
    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Contraseña generada ({longitud} caracteres): {password}")
    return password


def main():
    print("DEMOSTRACIÓN COMPLETA DE LA LIBRERÍA 'random'")
    demostrar_numeros_aleatorios()
    demostrar_selecciones_y_mezclas()
    demostrar_reproducibilidad()
    simulacion_lanzamiento_dados(10_000)
    caso_practico_generador_clave(16)
    print("\n" + "=" * 50)
    print("✓ Fin de la demostración de 'random'")
    print("=" * 50)


if __name__ == "__main__":
    main()
