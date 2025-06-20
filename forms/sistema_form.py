from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SistemaForm(FlaskForm):
    nombre = StringField('Nombre del Sistema', validators=[DataRequired()])
    sector = SelectField('Sector', choices=[('Salud', 'Salud'), ('Educación', 'Educación'), ('Finanzas', 'Finanzas'), ('Otro', 'Otro')])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    nivel_complejidad = SelectField('Nivel de Complejidad', choices=[('Bajo', 'Bajo'), ('Medio', 'Medio'), ('Alto', 'Alto')])
    uso_datos_personales = BooleanField('¿Usa Datos Personales?')
    tipo_aprendizaje = SelectField('Tipo de Aprendizaje', choices=[('Supervisado', 'Supervisado'), ('No Supervisado', 'No Supervisado')])
    nivel_intervencion_humana = SelectField('Nivel de Intervención Humana', choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')])
    submit = SubmitField('Registrar Sistema')
