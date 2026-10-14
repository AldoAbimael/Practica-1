"""
Ejemplo 01: Librería Estándar 'math'
====================================
Demostración de operaciones matemáticas avanzadas, constantes científicas,
trigonometría, redondeo, logaritmos, potencias y funciones combinatorias.
"""

import math
import sys

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def demostrar_constantes():
    print("\n" + "=" * 50)
    print(" 1. CONSTANTES MATEMÁTICAS FUNDAMENTALES")
    print("=" * 50)
    print(f"Pi (π)                 : {math.pi:.10f}")
    print(f"Número de Euler (e)    : {math.e:.10f}")
    print(f"Tau (τ = 2π)           : {math.tau:.10f}")
    print(f"Infinito positivo      : {math.inf}")
    print(f"Valor no numérico (NaN): {math.nan}")


def demostrar_trigonometria():
    print("\n" + "=" * 50)
    print(" 2. TRIGONOMETRÍA Y CONVERSIONES ANGULARES")
    print("=" * 50)
    angulo_grados = 45.0
    angulo_radianes = math.radians(angulo_grados)

    print(f"Ángulo en grados       : {angulo_grados}°")
    print(f"Conversión a radianes  : {angulo_radianes:.6f} rad")
    print(f"Conversión inversa     : {math.degrees(angulo_radianes):.1f}°")
    print(f"Seno (sin)             : {math.sin(angulo_radianes):.6f}")
    print(f"Coseno (cos)           : {math.cos(angulo_radianes):.6f}")
    print(f"Tangente (tan)         : {math.tan(angulo_radianes):.6f}")

    cateto_a, cateto_b = 3.0, 4.0
    hipotenusa = math.hypot(cateto_a, cateto_b)
    print(f"Hipotenusa de ({cateto_a}, {cateto_b}) : {hipotenusa}")


def demostrar_redondeo_y_enteros():
    print("\n" + "=" * 50)
    print(" 3. REDONDEO, TRUNCADO Y VALOR ABSOLUTO")
    print("=" * 50)
    numero = -7.685

    print(f"Número base            : {numero}")
    print(f"Valor absoluto (fabs)  : {math.fabs(numero)}")
    print(f"Techo (ceil, hacia +∞) : {math.ceil(numero)}")
    print(f"Piso (floor, hacia -∞) : {math.floor(numero)}")
    print(f"Truncado (trunc, a 0)  : {math.trunc(numero)}")


def demostrar_potencias_y_logaritmos():
    print("\n" + "=" * 50)
    print(" 4. POTENCIAS, RAÍCES Y LOGARITMOS")
    print("=" * 50)
    base = 2.0
    exponente = 10.0
    print(f"Potencia ({base}^{exponente})       : {math.pow(base, exponente)}")
    print(f"Raíz cuadrada de 144   : {math.sqrt(144)}")
    print(f"Raíz entera de 50      : {math.isqrt(50)}")
    print(f"Exponencial e^3        : {math.exp(3):.6f}")
    print(f"Logaritmo natural ln(e): {math.log(math.e):.1f}")
    print(f"Logaritmo base 10 (100): {math.log10(100):.1f}")
    print(f"Logaritmo base 2 (64)  : {math.log2(64):.1f}")


def demostrar_combinatoria_y_aritmetica():
    print("\n" + "=" * 50)
    print(" 5. COMBINATORIA Y TEORÍA DE NÚMEROS")
    print("=" * 50)
    n = 6
    k = 2
    print(f"Factorial de {n}!        : {math.factorial(n)}")
    print(f"Permutaciones P({n}, {k}) : {math.perm(n, k)}")
    print(f"Combinaciones C({n}, {k}) : {math.comb(n, k)}")

    num_a, num_b = 48, 18
    print(f"M.C.D. de ({num_a}, {num_b}) : {math.gcd(num_a, num_b)}")
    print(f"M.C.M. de ({num_a}, {num_b}) : {math.lcm(num_a, num_b)}")


def caso_practico_geometria():
    print("\n" + "=" * 50)
    print(" 6. CASO PRÁCTICO: FÍSICA Y GEOMETRÍA ANALÍTICA")
    print("=" * 50)
    # Distancia euclidiana 3D
    punto_a = (1.0, 2.0, 3.0)
    punto_b = (4.0, 6.0, 8.0)
    distancia_3d = math.dist(punto_a, punto_b)
    print(f"Distancia entre {punto_a} y {punto_b}: {distancia_3d:.4f}")

    # Área y volumen de una esfera de radio 5
    radio = 5.0
    area_circulo = math.pi * math.pow(radio, 2)
    volumen_esfera = (4.0 / 3.0) * math.pi * math.pow(radio, 3)
    print(f"Para radio = {radio}:")
    print(f"  - Área del círculo   : {area_circulo:.4f} u²")
    print(f"  - Volumen de la esfera: {volumen_esfera:.4f} u³")


def main():
    print("DEMOSTRACIÓN COMPLETA DE LA LIBRERÍA 'math'")
    demostrar_constantes()
    demostrar_trigonometria()
    demostrar_redondeo_y_enteros()
    demostrar_potencias_y_logaritmos()
    demostrar_combinatoria_y_aritmetica()
    caso_practico_geometria()
    print("\n" + "=" * 50)
    print("✓ Fin de la demostración de 'math'")
    print("=" * 50)


if __name__ == "__main__":
    main()
