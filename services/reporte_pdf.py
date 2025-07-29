from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
import os
import datetime

def generar_pdf(sistema, evaluaciones, certificacion):
    filename = f"static/reporte_sistema_{sistema['id']}.pdf"
    os.makedirs('static', exist_ok=True)
    c = canvas.Canvas(filename, pagesize=letter)

    # Encabezado
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 770, "Informe de Evaluación Ética – Registro Manual")
    c.setFont("Helvetica", 11)
    c.drawString(50, 755, f"Fecha de generación: {datetime.date.today().strftime('%d/%m/%Y')}")

    # Información del sistema
    c.setFont("Helvetica-Bold", 12)
    y = 730
    c.drawString(50, y, f"Nombre del sistema: {sistema['nombre']}")
    y -= 18
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Sector: {sistema['sector']}")
    y -= 16
    c.drawString(50, y, f"Nivel de complejidad: {sistema['nivel_complejidad']}")
    y -= 16
    c.drawString(50, y, f"Uso de datos personales: {'Sí' if sistema['uso_datos_personales'] else 'No'}")
    y -= 25

    # Evaluación ética
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Evaluación Ética:")
    y -= 18
    c.setFont("Helvetica", 11)
    for ev in evaluaciones:
        estado = "Cumple" if ev['resultado'] else "No cumple"
        c.drawString(60, y, f"- {ev['criterio']}: {estado}")
        y -= 14
        c.setFillColor(colors.grey)
        c.drawString(75, y, f"↳ {ev['observaciones']}")
        c.setFillColor(colors.black)
        y -= 18

    # Certificación
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Certificación:")
    y -= 18
    c.setFont("Helvetica", 11)
    c.drawString(60, y, f"Nivel: {certificacion['nivel']}")
    y -= 14
    c.drawString(60, y, f"Observaciones: {certificacion['obs']}")

    c.save()
    return filename


def generar_pdf_analisis(nombre_archivo, resultado, evaluaciones, riesgo, certificacion):
    nombre_pdf = f"static/reporte_{nombre_archivo}.pdf"
    os.makedirs('static', exist_ok=True)
    c = canvas.Canvas(nombre_pdf, pagesize=letter)

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 770, "Informe Ético de Análisis de Código")
    c.setFont("Helvetica", 11)
    c.drawString(50, 755, f"Archivo analizado: {nombre_archivo}")
    c.drawString(50, 740, f"Fecha: {datetime.date.today().strftime('%d/%m/%Y')}")

    y = 715

    # Indicadores técnicos
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Indicadores técnicos detectados:")
    y -= 20
    c.setFont("Helvetica", 11)
    for k, v in resultado.items():
        if isinstance(v, bool):
            c.drawString(60, y, f"- {k.replace('_', ' ').capitalize()}: {'Sí' if v else 'No'}")
            y -= 14

    y -= 15
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Evaluación Ética:")
    y -= 20
    c.setFont("Helvetica", 11)
    for ev in evaluaciones:
        estado = "Cumple" if ev['resultado'] else "No cumple"
        c.drawString(60, y, f"- {ev['criterio']}: {estado}")
        y -= 14
        c.setFillColor(colors.grey)
        c.drawString(75, y, f"↳ {ev['observaciones']}")
        c.setFillColor(colors.black)
        y -= 18

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Clasificación de riesgo:")
    y -= 16
    c.setFont("Helvetica", 11)
    c.drawString(60, y, f"Nivel de riesgo detectado: {riesgo}")

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Certificación:")
    y -= 16
    c.setFont("Helvetica", 11)
    c.drawString(60, y, f"Nivel: {certificacion['nivel']}")
    y -= 14
    c.drawString(60, y, f"Observaciones: {certificacion['obs']}")

    c.save()
    return nombre_pdf
