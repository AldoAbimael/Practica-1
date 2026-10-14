"""
Ejemplo 09: Visualización de Datos con 'Matplotlib'
==================================================
Generación de gráficos estadísticos de alta calidad estética:
- Gráfico de líneas (Evolución temporal con marcadores e intervalos)
- Gráfico de barras (Comparativa categórica con etiquetas de valor automáticas)
- Gráfico de dispersión (Scatter plot multivariable con mapa de colores)
- Exportación en alta resolución (PNG, 300 DPI) sin requerir servidor gráfico activo (Agg backend).
"""

import sys
from pathlib import Path
import matplotlib
# Configurar backend no interactivo para entornos de ejecución automáticos/servidores
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def configurar_estilos():
    """Aplica configuraciones visuales modernas y tipografía legible."""
    plt.rcParams["font.sans-serif"] = "DejaVu Sans"
    plt.rcParams["axes.edgecolor"] = "#CBD5E1"
    plt.rcParams["axes.linewidth"] = 0.8
    plt.rcParams["grid.color"] = "#E2E8F0"
    plt.rcParams["grid.linestyle"] = "--"
    plt.rcParams["grid.alpha"] = 0.7


def crear_dashboard_multipanel(ruta_guardado: Path):
    print("\n" + "=" * 50)
    print(" GENERANDO PANEL DE VISUALIZACIÓN MATPLOTLIB")
    print("=" * 50)

    configurar_estilos()

    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5), dpi=300)
    fig.suptitle("Dashboard Ejecutivo de Métricas de Negocio", fontsize=16, fontweight="bold", y=1.02, color="#0F172A")

    # -------------------------------------------------------------
    # 1. GRÁFICO DE LÍNEAS: Crecimiento Mensual
    # -------------------------------------------------------------
    ax1 = axes[0]
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct"]
    ventas_2025 = [22, 27, 25, 31, 38, 42, 40, 48, 53, 58]
    ventas_2026 = [28, 34, 39, 45, 52, 59, 63, 71, 78, 85]

    ax1.plot(meses, ventas_2025, marker="o", color="#94A3B8", linewidth=2, label="Año 2025")
    ax1.plot(meses, ventas_2026, marker="s", color="#2563EB", linewidth=2.5, label="Año 2026 (Actual)")

    ax1.set_title("Evolución de Ingresos Mensuales ($K)", fontsize=12, fontweight="bold", color="#1E293B", pad=10)
    ax1.set_ylabel("Monto en Miles de USD", fontsize=10, color="#475569")
    ax1.legend(frameon=True, facecolor="#F8FAFC", edgecolor="#CBD5E1")
    ax1.grid(True)
    ax1.tick_params(colors="#475569")

    # -------------------------------------------------------------
    # 2. GRÁFICO DE BARRAS: Rendimiento por Categoría
    # -------------------------------------------------------------
    ax2 = axes[1]
    categorias = ["SaaS", "Hardware", "Consultoría", "Soporte", "Formación"]
    valores = [142.5, 98.2, 75.0, 42.8, 31.4]
    colores_barras = ["#1E40AF", "#3B82F6", "#60A5FA", "#93C5FD", "#BFDBFE"]

    barras = ax2.bar(categorias, valores, color=colores_barras, width=0.6, edgecolor="#1E3A8A", linewidth=0.5)

    # Etiquetas numéricas sobre cada barra
    for barra in barras:
        altura = barra.get_height()
        ax2.annotate(
            f"${altura:.1f}K",
            xy=(barra.get_x() + barra.get_width() / 2, altura),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
            color="#1E293B",
        )

    ax2.set_title("Ventas Netas por Línea de Negocio", fontsize=12, fontweight="bold", color="#1E293B", pad=10)
    ax2.set_ylabel("Total Acumulado ($K)", fontsize=10, color="#475569")
    ax2.grid(axis="y")
    ax2.tick_params(colors="#475569")

    # -------------------------------------------------------------
    # 3. GRÁFICO DE DISPERSIÓN: Inversión en Ads vs Leads Calificados
    # -------------------------------------------------------------
    ax3 = axes[2]
    np.random.seed(42)
    inversion_marketing = np.random.uniform(5, 50, size=35)
    leads_obtenidos = inversion_marketing * 3.8 + np.random.normal(0, 12, size=35)
    tamano_burbuja = np.random.uniform(30, 250, size=35)  # Representa tamaño del cliente potencial

    scatter = ax3.scatter(
        inversion_marketing,
        leads_obtenidos,
        s=tamano_burbuja,
        c=leads_obtenidos,
        cmap="viridis",
        alpha=0.8,
        edgecolors="#334155",
        linewidths=0.5,
    )

    cbar = fig.colorbar(scatter, ax=ax3)
    cbar.set_label("Volumen de Conversión", fontsize=9, color="#475569")
    cbar.ax.tick_params(labelsize=8)

    ax3.set_title("Inversión en Campañas vs. Nuevos Leads", fontsize=12, fontweight="bold", color="#1E293B", pad=10)
    ax3.set_xlabel("Inversión Publicitaria ($K)", fontsize=10, color="#475569")
    ax3.set_ylabel("Leads Calificados", fontsize=10, color="#475569")
    ax3.grid(True)
    ax3.tick_params(colors="#475569")

    # Ajuste automático del lienzo
    plt.tight_layout()
    plt.savefig(ruta_guardado, format="png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"✓ Gráfico multivariable generado exitosamente en:\n  {ruta_guardado}")


def main():
    print("DEMOSTRACIÓN COMPLETA DE LA LIBRERÍA 'matplotlib'")
    archivo_imagen = OUTPUT_DIR / "dashboard_metricas_matplotlib.png"
    crear_dashboard_multipanel(archivo_imagen)
    print("\n" + "=" * 50)
    print("✓ Fin de la demostración de 'matplotlib'")
    print("=" * 50)


if __name__ == "__main__":
    main()
