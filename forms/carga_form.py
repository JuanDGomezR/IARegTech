from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class CargaArchivoForm(FlaskForm):
    nombre = StringField('Nombre del Proyecto', validators=[DataRequired()])
    archivo = FileField('Archivo del Proyecto IA', validators=[
        FileAllowed(['py', 'ipynb', 'pkl', 'csv', 'txt'], 'Solo se permiten archivos .py, .ipynb, .pkl, .csv, .txt'),
        DataRequired()
    ])
    submit = SubmitField('Subir y Analizar')
