"""
Ejemplo 10: Consumo de APIs REST con 'requests'
===============================================
Interacción HTTP completa con el servicio público JSONPlaceholder:
- Peticiones GET individuales y con parámetros de consulta (query params)
- Peticiones POST enviando estructuras serializadas en formato JSON
- Inspección de cabeceras, códigos de estado HTTP y tiempos de respuesta
- Manejo profesional de errores (timeouts, 404 Not Found, excepciones de red)
"""

import json
import sys
import requests
from requests.exceptions import HTTPError, RequestException, Timeout

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


BASE_URL = "https://jsonplaceholder.typicode.com"
HEADERS_BASE = {
    "User-Agent": "CursoPythonAvanzado/1.0",
    "Accept": "application/json",
}


def realizar_get_individual(post_id: int = 1):
    print("\n" + "=" * 50)
    print(f" 1. PETICIÓN HTTP GET - RECURSO INDIVIDUAL (/posts/{post_id})")
    print("=" * 50)
    url = f"{BASE_URL}/posts/{post_id}"

    try:
        respuesta = requests.get(url, headers=HEADERS_BASE, timeout=10)
        respuesta.raise_for_status()  # Genera excepción si el código es 4xx o 5xx

        print(f"URL consultada         : {respuesta.url}")
        print(f"Código de estado HTTP  : {respuesta.status_code} {respuesta.reason}")
        print(f"Tiempo de respuesta    : {respuesta.elapsed.total_seconds():.3f} segundos")
        print(f"Tipo de contenido      : {respuesta.headers.get('Content-Type')}")

        datos = respuesta.json()
        print("\nCuerpo de la respuesta (JSON parseado):")
        print(f"  - ID      : {datos['id']}")
        print(f"  - Usuario : {datos['userId']}")
        print(f"  - Título  : {datos['title']}")
        print(f"  - Mensaje : {datos['body'][:60]}...")

    except HTTPError as http_err:
        print(f"Error HTTP ocurrido: {http_err}")
    except Timeout:
        print("La solicitud superó el tiempo límite de espera.")
    except RequestException as err:
        print(f"Error general de red: {err}")


def realizar_get_con_parametros(user_id: int = 1):
    print("\n" + "=" * 50)
    print(f" 2. PETICIÓN HTTP GET CON QUERY PARAMS (/posts?userId={user_id})")
    print("=" * 50)
    url = f"{BASE_URL}/posts"
    parametros = {"userId": user_id}

    try:
        respuesta = requests.get(url, params=parametros, headers=HEADERS_BASE, timeout=10)
        respuesta.raise_for_status()

        print(f"URL final generada     : {respuesta.url}")
        publicaciones = respuesta.json()
        print(f"Total de posts hallados: {len(publicaciones)}")
        print("\nPrimeros 2 posts obtenidos:")
        for post in publicaciones[:2]:
            print(f"  • [Post #{post['id']}] {post['title']}")

    except RequestException as err:
        print(f"Error al consultar lista con parámetros: {err}")


def realizar_post_creacion():
    print("\n" + "=" * 50)
    print(" 3. PETICIÓN HTTP POST - CREACIÓN DE RECURSO (/posts)")
    print("=" * 50)
    url = f"{BASE_URL}/posts"
    nuevo_post = {
        "title": "Arquitectura de Software en Python",
        "body": "Patrones de diseño, tipado estático y pruebas automatizadas en sistemas distribuidos.",
        "userId": 99,
    }

    try:
        # requests serializa automáticamente diccionarios pasados a 'json=' y configura 'Content-Type: application/json'
        respuesta = requests.post(url, json=nuevo_post, headers=HEADERS_BASE, timeout=10)
        respuesta.raise_for_status()

        print(f"Código de estado HTTP  : {respuesta.status_code} (Recurso Creado)")
        datos_creados = respuesta.json()
        print("\nRespuesta del servidor:")
        print(json.dumps(datos_creados, indent=2, ensure_ascii=False))

    except RequestException as err:
        print(f"Error al enviar datos POST: {err}")


def demostrar_manejo_de_errores():
    print("\n" + "=" * 50)
    print(" 4. MANEJO PROFESIONAL DE ERRORES HTTP (Ejemplo 404 Not Found)")
    print("=" * 50)
    url_inexistente = f"{BASE_URL}/recurso_no_existente_404"

    try:
        respuesta = requests.get(url_inexistente, timeout=5)
        respuesta.raise_for_status()
    except HTTPError as error:
        print(f"✓ Error HTTP capturado de forma controlada:")
        print(f"  - Código: {error.response.status_code}")
        print(f"  - Mensaje del servidor: {error.response.reason}")
    except RequestException as error:
        print(f"Error de conexión: {error}")


def main():
    print("DEMOSTRACIÓN COMPLETA DE LA LIBRERÍA 'requests'")
    realizar_get_individual(1)
    realizar_get_con_parametros(1)
    realizar_post_creacion()
    demostrar_manejo_de_errores()
    print("\n" + "=" * 50)
    print("✓ Fin de la demostración de 'requests'")
    print("=" * 50)


if __name__ == "__main__":
    main()
