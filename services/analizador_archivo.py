PALABRAS_IA = [
    'sklearn', 'tensorflow', 'keras', 'torch', 'xgboost', 'pytorch', 'scipy', 'numpy',
    'pandas', 'matplotlib', 'seaborn', 'jupyter', 'colab', 'gpu', 'cpu', 'api',
    'modelo', 'algoritmo', 'entrenamiento', 'predicción', 'clasificación', 'regresión',
    'clusterización', 'red_neuronal', 'deep_learning', 'machine_learning',
    'inteligencia_artificial', 'overfitting', 'underfitting', 'validación',
    'hiperparámetros', 'feature_engineering', 'datos_de_entrenamiento',
    'datos_de_prueba', 'optimización', 'gradiente', 'convolucional', 'recurrente',
    'transformer', 'atención'
]

PALABRAS_DATOS = [
    'pandas', 'read_csv', 'open(', '.csv', 'json.load', 'excel', 'sql', 'database',
    'dataframe', 'series', 'filas', 'columnas', 'índices', 'filtrar', 'agrupar',
    'pivotar', 'mergear', 'unir', 'limpieza', 'preprocesamiento', 'missing_values',
    'outliers', 'visualización', 'grafico', 'histograma', 'scatterplot', 'boxplot',
    'etl', 'data_lake', 'data_warehouse', 'big_data', 'streaming', 'no_sql', 'cloud'
]

PALABRAS_DECISION = [
    'predict', 'fit(', 'transform', 'classify', 'regresión', 'clustering', 'evaluar',
    'métricas', 'precisión', 'recall', 'f1_score', 'auc', 'error', 'sesgo',
    'varianza', 'umbral', 'decisión', 'regla', 'criterio', 'optimizar', 'seleccionar',
    'elegir', 'validar', 'interpretar', 'inferir', 'generalizar', 'desplegar',
    'monitorizar', 'ajustar', 'actualizar', 'rollback', 'go_no_go'
]

PALABRAS_SENSIBLES = [
    'edad', 'sexo', 'raza', 'género', 'ingreso', 'puta', 'discapacidad', 'salud',
    'enfermedad', 'historial_médico', 'orientación_sexual', 'identidad_de_género',
    'religión', 'etnia', 'nacionalidad', 'afiliación_política', 'antecedentes_penales',
    'datos_biométricos', 'genéticos', 'hijos', 'estado_civil', 'dirección', 'teléfono',
    'correo_electrónico', 'historial_crediticio', 'situación_laboral',
    'opiniones_políticas', 'vida_sexual', 'afiliaciones_sindicales', 'filosóficas'
]

PALABRAS_SENSIBLES_EXT = [
    'religion', 'etnia', 'orientacion', 'discapacidad', 'diagnostico', 'nacionalidad',
    'afiliación_política', 'antecedentes_penales', 'datos_biométricos', 'genéticos',
    'hijos', 'estado_civil', 'dirección', 'teléfono', 'correo_electrónico',
    'historial_crediticio', 'situación_laboral', 'opiniones_políticas', 'vida_sexual',
    'afiliaciones_sindicales', 'filosóficas', 'familia', 'salud_mental',
    'historial_familiar', 'reclamaciones_de_seguro', 'información_financiera',
    'educación', 'carrera_profesional', 'redes_sociales', 'preferencias_de_consumo',
    'ubicación_geográfica'
]

PALABRAS_EXPLICABILIDAD = [
    'shap', 'lime', 'decisiontree', 'plot_importance', 'interpretabilidad',
    'explicabilidad', 'transparencia', 'razones', 'contribución', 'relevancia',
    'influencia', 'factores', 'pesos', 'coeficientes', 'atributos', 'características',
    'visualización', 'mapas_de_calor', 'árboles_de_decisión', 'reglas',
    'contrafactuals', 'perturbación', 'sensibilidad', 'robustez', 'auditoría', 'ética',
    'justicia', 'responsabilidad', 'confianza', 'cajas_negras', 'cajas_blancas',
    'local', 'global'
]

PALABRAS_DOC = [
    '"""', '"""', '# ', '# TODO', 'docstring', 'comentario', 'documentación', 'guía',
    'manual', 'ejemplo', 'tutorial', 'api', 'referencia', 'markdown', 'rst', 'sphinx',
    'readthedocs', 'autodoc', 'pydoc', 'wiki', 'kb', 'faq', 'issue_tracker',
    'changelog', 'versión', 'copyright', 'licencia', 'autor', 'fecha', 'descripción',
    'parámetros', 'retorna', 'excepciones', 'notas'
]

PALABRAS_LICENCIA = [
    'license', 'mit', 'gpl', 'apache', 'bsd', 'mozilla', 'epl', 'lgpl', 'cc',
    'public_domain', 'copyleft', 'permissive', 'restrictiva', 'derechos_de_autor',
    'patente', 'marca_registrada', 'código_abierto', 'software_libre', 'privativo',
    'uso_comercial', 'distribución', 'modificación', 'sublicencia', 'atribución',
    'no_derivados', 'compartir_igual', 'renuncia_de_garantía',
    'limitación_de_responsabilidad', 'acuerdo'
]

PALABRAS_CONSENTIMIENTO = [
    'consentimiento', 'autorizacion', 'permiso', 'acuerdo', 'aceptación', 'aprobación',
    'expreso', 'implícito', 'informado', 'revocable', 'términos', 'condiciones',
    'política_de_privacidad', 'uso_de_datos', 'recolección_de_datos',
    'almacenamiento_de_datos', 'tratamiento_de_datos', 'compartir_datos', 'finalidades',
    'derechos_del_titular', 'retirada_del_consentimiento', 'opt_in', 'opt_out',
    'cookies', 'gdpr', 'ccpa', 'ley_de_protección_de_datos', 'regulaciones',
    'legitimidad', 'base_legal', 'transparencia', 'control'
]
def fue_generado_por_ia(contenido):
    patrones_sospechosos = [
        'This function', 'def my_function', 'model =', 'import numpy as np',
        'if __name__ == "__main__"', '# TODO', 'X =', 'y ='
    ]
    return sum(1 for p in patrones_sospechosos if p.lower() in contenido.lower()) >= 2

def analizar_codigo(path_archivo):
    try:
        with open(path_archivo, 'r', encoding='utf-8', errors='ignore') as f:
            contenido = f.read().lower()
    except Exception as e:
        return {'error': str(e)}

    resultado = {
        'usa_ia': any(p in contenido for p in PALABRAS_IA),
        'procesa_datos': any(p in contenido for p in PALABRAS_DATOS),
        'automatiza_decisiones': any(p in contenido for p in PALABRAS_DECISION),
        'usa_variables_sensibles': any(p in contenido for p in PALABRAS_SENSIBLES),
        'sospecha_ia': fue_generado_por_ia(contenido),
        'usa_datos_sensibles_extendidos': any(p in contenido for p in PALABRAS_SENSIBLES_EXT),
        'incluye_documentacion': any(p in contenido for p in PALABRAS_DOC),
        'usa_modelos_explicables': any(p in contenido for p in PALABRAS_EXPLICABILIDAD),
        'usa_autonomia_alta': 'if predict' in contenido or 'while predict' in contenido,
        'incluye_licencia': any(p in contenido for p in PALABRAS_LICENCIA),
        'requiere_consentimiento': any(p in contenido for p in PALABRAS_CONSENTIMIENTO),
    }

    resultado['riesgo_potencial'] = (
        resultado['usa_ia'] and resultado['automatiza_decisiones'] and (
            resultado['usa_variables_sensibles'] or resultado['usa_datos_sensibles_extendidos']
        )
    )

    return resultado
