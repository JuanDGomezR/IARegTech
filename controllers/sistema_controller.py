from flask import Blueprint, render_template, request, redirect, url_for
from forms.sistema_form import SistemaForm
from models.sistema import SistemaIA
from services.clasificador import ClasificadorRiesgo
from services.certificador import generar_certificacion
from services.reporte_pdf import generar_pdf
from services.notificador import enviar_notificacion
from extensions import mysql
sistema_bp = Blueprint('sistema', __name__)

@sistema_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = SistemaForm()
    if form.validate_on_submit():
        sistema = SistemaIA(
            nombre=form.nombre.data,
            sector=form.sector.data,
            descripcion=form.descripcion.data,
            nivel_complejidad=form.nivel_complejidad.data,
            uso_datos_personales=form.uso_datos_personales.data,
            tipo_aprendizaje=form.tipo_aprendizaje.data,
            nivel_intervencion_humana=form.nivel_intervencion_humana.data
        )
        sistema.guardar()
        return redirect(url_for('sistema.evaluar', id=sistema.id))
    return render_template('registrar.html', form=form)

@sistema_bp.route('/evaluar/<int:id>', methods=['GET'])
def evaluar(id):
    sistema = SistemaIA.obtener(id)
    resultados = sistema.evaluar_etica()
    return render_template('evaluacion_resultado.html', resultados=resultados)

@sistema_bp.route('/clasificar/<int:id>')
def clasificar(id):
    sistema_dict = SistemaIA.obtener_como_dict(id)
    clasificador = ClasificadorRiesgo(sistema_dict)
    nivel = clasificador.clasificar()
    return f"Clasificación de riesgo: {nivel}"

@sistema_bp.route('/certificar/<int:id>')
def certificar(id):
    sistema_dict = SistemaIA.obtener_como_dict(id)
    certificacion = generar_certificacion(sistema_dict)
    return f"Certificación: {certificacion['nivel']} – {certificacion['obs']}"

@sistema_bp.route('/reporte/<int:id>', methods=['GET'])
def reporte(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sistemas_ia WHERE id = %s", (id,))
    data = cur.fetchone()
    keys = [desc[0] for desc in cur.description]
    sistema = dict(zip(keys, data))

    cur.execute("SELECT * FROM evaluaciones_eticas WHERE sistema_id = %s", (id,))
    evaluaciones_raw = cur.fetchall()
    evaluaciones = [
        {'criterio': row[2], 'resultado': row[3], 'observaciones': row[4]}
        for row in evaluaciones_raw
    ]

    cur.execute("SELECT * FROM certificados WHERE sistema_id = %s", (id,))
    cert_raw = cur.fetchone()
    if not cert_raw:
        return "No se encontró una certificación para este sistema. Certifícalo primero."

    certificacion = {'nivel': cert_raw[2], 'obs': cert_raw[3]}
    cur.close()

    ruta_pdf = generar_pdf(sistema, evaluaciones, certificacion)

    # Puedes reactivar este bloque si decides enviar correos:
    # enviar_notificacion(
    #     destinatario='destinatario@example.com',
    #     asunto='Informe de Certificación de Sistema IA',
    #     cuerpo='Se adjunta el informe de evaluación y certificación.',
    #     adjunto_path=ruta_pdf
    # )

    return f"Informe generado: <a href='/{ruta_pdf}' target='_blank'>Descargar PDF</a>"

# ✅ NUEVA RUTA: Listar todos los sistemas evaluados
@sistema_bp.route('/sistemas')
def listar_sistemas():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT s.id, s.nombre, s.sector, s.fecha_creacion,
               c.nivel_aprobacion as certificacion, s.riesgo
        FROM sistemas_ia s
        LEFT JOIN certificados c ON s.id = c.sistema_id
        ORDER BY s.fecha_creacion DESC
    """)
    sistemas = cur.fetchall()
    cur.close()
    return render_template('listar_sistemas.html', sistemas=sistemas)

