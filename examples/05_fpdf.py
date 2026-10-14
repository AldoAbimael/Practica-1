"""
Ejemplo 05: Generación de PDF con 'fpdf2'
=========================================
Creación de un documento PDF profesional con:
- Cabecera y pie de página dinámicos (Paginación automática)
- Estilos tipográficos, colores corporativos y geometrías
- Celdas simples y multiceldas para párrafos con salto de línea
- Construcción de tablas estilizadas con filas intercaladas
"""

import sys
from pathlib import Path
from fpdf import FPDF

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class ReporteCorporativoPDF(FPDF):
    """Subclase de FPDF para personalizar la plantilla corporativa."""

    def header(self):
        # Título principal
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(26, 54, 93)  # Azul corporativo oscuro
        self.cell(0, 8, "SISTEMA DE GESTIÓN EMPRESARIAL", align="C")
        self.ln(6)

        # Subtítulo institucional
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 116, 139)
        self.cell(0, 6, "Reporte Ejecutivo de Rendimiento y Operaciones", align="C")
        self.ln(8)

        # Línea divisoria decorativa
        self.set_draw_color(203, 213, 225)
        self.set_line_width(0.5)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(5)

    def footer(self):
        # Posición a 15 mm del borde inferior
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(148, 163, 184)
        # Línea de cierre
        self.set_draw_color(226, 232, 240)
        self.line(self.l_margin, self.get_y() - 2, self.w - self.r_margin, self.get_y() - 2)
        # Paginación
        self.cell(0, 10, f"Documento confidencial | Página {self.page_no()}/{{nb}}", align="C")


def generar_pdf_ejecutivo(ruta_destino: Path):
    pdf = ReporteCorporativoPDF(orientation="P", unit="mm", format="A4")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # 1. Sección de Introducción / Resumen
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 10, "1. Resumen Ejecutivo del Periodo", align="L")
    pdf.ln(8)

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(51, 65, 85)
    texto_resumen = (
        "El presente informe detalla el progreso y métricas operativas de la organización durante "
        "el último trimestre. Se destaca un incremento del 18.5% en la eficiencia de entregas y "
        "una optimización sostenida en el consumo de recursos computacionales. Los datos presentados "
        "a continuación han sido auditados según los estándares de calidad vigentes."
    )
    pdf.multi_cell(0, 6, texto_resumen)
    pdf.ln(6)

    # 2. Caja destacada (KPI principal)
    pdf.set_fill_color(241, 245, 249)
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(x=pdf.l_margin, y=pdf.get_y(), w=170, h=18, style="DF")
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(170, 9, "  KPI CLAVE: Tasa de Disponibilidad del Servicio (SLA): 99.94%", align="L")
    pdf.ln(9)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(170, 9, "  Objetivo anual superado en un +0.44% sin incidentes críticos registrados.", align="L")
    pdf.ln(14)

    # 3. Tabla de Rendimiento por Proyecto
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 10, "2. Métricas de Desempeño por Proyecto", align="L")
    pdf.ln(8)

    # Cabecera de la tabla
    columnas = [
        ("Código", 28),
        ("Proyecto", 62),
        ("Responsable", 45),
        ("Presupuesto", 35),
    ]

    pdf.set_fill_color(30, 64, 175)  # Azul oscuro
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_draw_color(30, 64, 175)

    for col_titulo, col_ancho in columnas:
        pdf.cell(col_ancho, 8, col_titulo, border=1, align="C", fill=True)
    pdf.ln()

    # Filas de la tabla
    datos_tabla = [
        ("PRJ-001", "Migración Cloud AWS", "Ing. A. Morales", "$45,000 USD"),
        ("PRJ-002", "App Móvil Clientes v2", "Lic. S. Herrera", "$28,500 USD"),
        ("PRJ-003", "Pipeline de Datos ML", "Dr. E. Benítez", "$62,000 USD"),
        ("PRJ-004", "Portal de Facturación", "Ing. M. Torres", "$19,800 USD"),
        ("PRJ-005", "Auditoría de Ciberseguridad", "Mtra. K. Rivas", "$34,200 USD"),
    ]

    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(30, 41, 59)
    pdf.set_draw_color(226, 232, 240)

    for i, fila in enumerate(datos_tabla):
        # Alternancia de color de fondo en filas
        if i % 2 == 0:
            pdf.set_fill_color(248, 250, 252)
        else:
            pdf.set_fill_color(255, 255, 255)

        for col_idx, valor in enumerate(fila):
            ancho = columnas[col_idx][1]
            alineacion = "C" if col_idx in (0, 3) else "L"
            pdf.cell(ancho, 7, valor, border=1, align=alineacion, fill=True)
        pdf.ln()

    # Guardar archivo PDF
    pdf.output(str(ruta_destino))
    print(f"✓ PDF generado exitosamente con 'fpdf2' en:\n  {ruta_destino}")


def main():
    print("DEMOSTRACIÓN COMPLETA DE LA LIBRERÍA 'fpdf2'")
    archivo_pdf = OUTPUT_DIR / "reporte_ejecutivo_fpdf.pdf"
    generar_pdf_ejecutivo(archivo_pdf)
    print("\n" + "=" * 50)
    print("✓ Fin de la demostración de 'fpdf2'")
    print("=" * 50)


if __name__ == "__main__":
    main()
