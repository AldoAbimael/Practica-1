"""
Ejemplo 06: Generación de PDF con 'ReportLab'
============================================
Creación de documentos PDF de nivel editorial y corporativo combinando:
- El motor de flujo Platypus (SimpleDocTemplate, Paragraph, Spacer, Table)
- Control de bajo nivel con Canvas para membretes, numeración y marcas de agua
- Estilos tipográficos avanzados (getSampleStyleSheet, ParagraphStyle)
- Tablas estilizadas con reportlab.lib.colors
"""

import sys
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class NumeradorPaginas(canvas.Canvas):
    """Canvas personalizado de dos pasadas para calcular y numerar páginas dinámicamente."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.paginas = []

    def showPage(self):
        self.paginas.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_total_paginas = len(self.paginas)
        for estado_pagina in self.paginas:
            self.__dict__.update(estado_pagina)
            self.dibujar_elementos_fijos(num_total_paginas)
            super().showPage()
        super().save()

    def dibujar_elementos_fijos(self, total_paginas: int):
        # 1. Membrete superior con Canvas
        self.saveState()
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(2 * cm, 28 * cm, A4[0] - 2 * cm, 28 * cm)

        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#475569"))
        self.drawString(2 * cm, 28.3 * cm, "INFORME TÉCNICO DE ARQUITECTURA")
        self.drawRightString(A4[0] - 2 * cm, 28.3 * cm, "ESTRICTAMENTE CONFIDENCIAL")

        # 2. Pie de página con Canvas
        self.line(2 * cm, 2 * cm, A4[0] - 2 * cm, 2 * cm)
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(2 * cm, 1.5 * cm, "Generado automáticamente por ReportLab 4.x")
        self.drawRightString(
            A4[0] - 2 * cm,
            1.5 * cm,
            f"Página {self._pageNumber} de {total_paginas}",
        )
        self.restoreState()


def generar_pdf_reportlab(ruta_destino: Path):
    doc = SimpleDocTemplate(
        str(ruta_destino),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
    )

    estilos = getSampleStyleSheet()

    # Creación de estilos personalizados
    estilo_titulo = ParagraphStyle(
        "TituloPrincipal",
        parent=estilos["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0F172A"),
        alignment=0,  # Izquierda
        spaceAfter=10,
    )

    estilo_subtitulo = ParagraphStyle(
        "Subtitulo",
        parent=estilos["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=16,
        textColor=colors.HexColor("#334155"),
        spaceAfter=15,
    )

    estilo_seccion = ParagraphStyle(
        "SeccionHeader",
        parent=estilos["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=18,
        textColor=colors.HexColor("#1E3A8A"),
        spaceBefore=12,
        spaceAfter=8,
    )

    estilo_cuerpo = ParagraphStyle(
        "Cuerpo",
        parent=estilos["BodyText"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=8,
    )

    historia = []

    # Título y metadatos
    historia.append(Paragraph("Evaluación de Escalabilidad y Microservicios", estilo_titulo))
    historia.append(
        Paragraph("División de Ingeniería de Software | Auditoría de Cómputo Distribuido", estilo_subtitulo)
    )
    historia.append(Spacer(1, 0.4 * cm))

    # Sección 1: Análisis Descriptivo
    historia.append(Paragraph("1. Diagnóstico del Sistema y Métricas de Rendimiento", estilo_seccion))
    texto_diagnostico = (
        "Durante el periodo de análisis bajo cargas pico de 50,000 peticiones por minuto, "
        "la latencia P99 se mantuvo en <b>124 ms</b>, evidenciando un desempeño óptimo en la capa "
        "de orquestación mediante Kubernetes y balanceadores de carga de capa 7."
    )
    historia.append(Paragraph(texto_diagnostico, estilo_cuerpo))
    historia.append(Spacer(1, 0.3 * cm))

    # Sección 2: Tabla Estilizada con Flowables
    historia.append(Paragraph("2. Tabla de Microservicios Evaluados", estilo_seccion))

    encabezado_tabla = ["Microservicio", "Tecnología", "Latencia P95", "Disponibilidad", "Estado"]
    filas_datos = [
        ["Auth Service", "Go / OAuth2", "42 ms", "99.99%", "Aprobado"],
        ["Billing API", "Python / FastAPI", "78 ms", "99.95%", "Aprobado"],
        ["Search Core", "Rust / Tantivy", "18 ms", "99.98%", "Excelente"],
        ["Notification Hub", "Node.js / Redis", "110 ms", "99.85%", "En Observación"],
        ["Data Warehouse Sync", "Python / DuckDB", "145 ms", "99.90%", "Aprobado"],
    ]

    contenido_tabla = [encabezado_tabla] + filas_datos

    tabla = Table(contenido_tabla, colWidths=[3.8 * cm, 3.4 * cm, 2.5 * cm, 2.8 * cm, 3.5 * cm])
    tabla.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E3A8A")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 9),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 7),
                ("TOPPADDING", (0, 0), (-1, 0), 7),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("ALIGN", (0, 1), (0, -1), "LEFT"),  # Alinear nombres a la izquierda
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 1), (-1, -1), 8.5),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F8FAFC"), colors.white]),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    historia.append(tabla)
    historia.append(Spacer(1, 0.6 * cm))

    # Sección 3: Conclusiones
    historia.append(Paragraph("3. Dictamen y Próximos Pasos", estilo_seccion))
    conclusiones = (
        "Se recomienda autorizar el despliegue a producción de la versión 2.4. "
        "El microservicio <i>Notification Hub</i> deberá ser sometido a un profiling de memoria "
        "antes de alcanzar la temporada comercial alta."
    )
    historia.append(Paragraph(conclusiones, estilo_cuerpo))

    # Compilar el documento usando el canvas de doble pasada
    doc.build(historia, canvasmaker=NumeradorPaginas)
    print(f"✓ PDF estructurado generado exitosamente con 'ReportLab' en:\n  {ruta_destino}")


def main():
    print("DEMOSTRACIÓN COMPLETA DE LA LIBRERÍA 'reportlab'")
    archivo_pdf = OUTPUT_DIR / "reporte_estructurado_reportlab.pdf"
    generar_pdf_reportlab(archivo_pdf)
    print("\n" + "=" * 50)
    print("✓ Fin de la demostración de 'reportlab'")
    print("=" * 50)


if __name__ == "__main__":
    main()
