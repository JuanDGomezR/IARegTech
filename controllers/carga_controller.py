import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from forms.carga_form import CargaArchivoForm
from services.analizador_archivo import analizar_codigo
from services.evaluador_automatico import evaluar_etica_desde_analisis
from services.clasificador_automatico import clasificar_riesgo
from services.certificador_automatico import emitir_certificacion
from services.reporte_pdf import generar_pdf_analisis

carga_bp = Blueprint('carga', __name__)
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'py', 'txt'}

# ✅ Función para verificar extensión permitida
def extension_permitida(nombre_archivo):
    return '.' in nombre_archivo and nombre_archivo.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@carga_bp.route('/subir', methods=['GET', 'POST'])
def subir_archivo():
    form = CargaArchivoForm()
    if form.validate_on_submit():
        archivo = form.archivo.data
        nombre = form.nombre.data
        nombre_archivo = secure_filename(archivo.filename)

        # ✅ Validar extensión
        if not extension_permitida(nombre_archivo):
            flash("⚠️ Tipo de archivo no permitido. Solo se aceptan archivos con extensión .py y .txt", "danger")
            return redirect(url_for('carga.subir_archivo'))

        ruta = os.path.join(UPLOAD_FOLDER, nombre_archivo)
        archivo.save(ruta)
        return redirect(url_for('carga.analizar_archivo', filename=nombre_archivo))
    
    return render_template('subir_archivo.html', form=form)

@carga_bp.route('/analizar/<filename>', methods=['GET'])
def analizar_archivo(filename):
    ruta = os.path.join('uploads', filename)
    resultado = analizar_codigo(ruta)

    if 'error' in resultado:
        return f"Error al analizar el archivo: {resultado['error']}"

    evaluaciones = evaluar_etica_desde_analisis(resultado)
    riesgo = clasificar_riesgo(resultado)
    certificacion = emitir_certificacion(riesgo)
    ruta_pdf = generar_pdf_analisis(filename, resultado, evaluaciones, riesgo, certificacion)

    return render_template(
        'resultado_analisis.html',
        filename=filename,
        resultado=resultado,
        evaluaciones=evaluaciones,
        riesgo=riesgo,
        certificacion=certificacion,
        ruta_pdf=ruta_pdf
    )
