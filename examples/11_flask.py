"""
Ejemplo 11: Microservicios Web y API REST con 'Flask'
=====================================================
Desarrollo de una API RESTful minimalista y modular:
- Ruta raíz informativa ('/') con documentación de endpoints
- Endpoint JSON estructurado ('/api/v1/products') con filtrado mediante query params
- Endpoint individual ('/api/v1/products/<id>') con validación y manejo de error 404
- Respuestas estandarizadas en formato JSON y códigos de estado HTTP
"""

import sys
from flask import Flask, jsonify, request

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


app = Flask(__name__)
# Evitar ordenamiento alfabético automático de claves JSON en Flask 2.3+ / 3.x
app.json.sort_keys = False

# Base de datos en memoria para la demostración
PRODUCTOS_DB = [
    {"id": 1, "nombre": "Laptop Ultrabook Pro", "categoria": "Computo", "precio": 1250.00, "stock": 15},
    {"id": 2, "nombre": "Mouse Inalámbrico RGB", "categoria": "Perifericos", "precio": 35.50, "stock": 50},
    {"id": 3, "nombre": "Monitor Curvo 34p", "categoria": "Monitores", "precio": 540.00, "stock": 8},
    {"id": 4, "nombre": "Teclado Mecánico Custom", "categoria": "Perifericos", "precio": 110.00, "stock": 25},
    {"id": 5, "nombre": "Auriculares Cancelación Ruido", "categoria": "Audio", "precio": 180.00, "stock": 30},
]


@app.route("/", methods=["GET"])
def pagina_inicio():
    """Ruta 1: Página principal informativa de la API."""
    return jsonify(
        {
            "servicio": "API Catálogo de Productos",
            "version": "1.0.0",
            "estado": "Activo / Operacional",
            "endpoints_disponibles": {
                "listar_productos": "GET /api/v1/products",
                "filtrar_por_categoria": "GET /api/v1/products?categoria=Perifericos",
                "filtrar_por_precio_max": "GET /api/v1/products?max_precio=200",
                "consultar_producto_id": "GET /api/v1/products/<int:id>",
            },
            "instruccion": "Visita /api/v1/products en tu navegador o cliente HTTP.",
        }
    )


@app.route("/api/v1/products", methods=["GET"])
def listar_productos():
    """Ruta 2: Endpoint REST que devuelve la lista de productos con soporte para filtros."""
    categoria = request.args.get("categoria", type=str)
    max_precio = request.args.get("max_precio", type=float)

    resultados = PRODUCTOS_DB

    if categoria:
        resultados = [p for p in resultados if p["categoria"].lower() == categoria.lower()]

    if max_precio is not None:
        resultados = [p for p in resultados if p["precio"] <= max_precio]

    return jsonify(
        {
            "total_items": len(resultados),
            "filtros_aplicados": {"categoria": categoria, "max_precio": max_precio},
            "data": resultados,
        }
    ), 200


@app.route("/api/v1/products/<int:product_id>", methods=["GET"])
def obtener_producto_por_id(product_id: int):
    """Endpoint individual: Retorna el producto correspondiente o un error 404 estructurado."""
    producto = next((p for p in PRODUCTOS_DB if p["id"] == product_id), None)
    if producto is None:
        return jsonify(
            {
                "status": 404,
                "error": "Recurso No Encontrado",
                "mensaje": f"No se encontró ningún producto con ID {product_id}.",
            }
        ), 404

    return jsonify({"status": 200, "data": producto}), 200


@app.errorhandler(404)
def recurso_no_encontrado(error):
    """Manejador global para rutas inexistentes devolviendo JSON."""
    return jsonify({"status": 404, "error": "Ruta no encontrada", "mensaje": str(error)}), 404


def main():
    print("=" * 60)
    print(" SERVICIO API REST FLASK LISTO PARA INICIAR")
    print("=" * 60)
    print("Servidor en ejecución en: http://127.0.0.1:5000")
    print("Endpoints listos:")
    print("  - http://127.0.0.1:5000/")
    print("  - http://127.0.0.1:5000/api/v1/products")
    print("  - http://127.0.0.1:5000/api/v1/products?categoria=Perifericos")
    print("  - http://127.0.0.1:5000/api/v1/products/1")
    print("Presiona Ctrl+C en la terminal para detener el servidor.\n")
    app.run(host="127.0.0.1", port=5000, debug=True)


if __name__ == "__main__":
    main()
