def evaluar_etica_desde_analisis(resultado_analisis):
    evaluaciones = []

    # Transparencia
    cumple_transparencia = resultado_analisis['usa_ia'] and not resultado_analisis['automatiza_decisiones']
    observacion_transparencia = (
        'Uso de IA con intervención humana' if cumple_transparencia
        else 'Falta evidencia de intervención humana.'
    )
    evaluaciones.append({
        'criterio': 'Transparencia',
        'resultado': cumple_transparencia,
        'observaciones': observacion_transparencia
    })

    # No Discriminación
    evaluaciones.append({
        'criterio': 'No Discriminación',
        'resultado': not resultado_analisis['usa_variables_sensibles'],
        'observaciones': (
            'No se encontraron variables sensibles'
            if not resultado_analisis['usa_variables_sensibles']
            else 'Se usan variables potencialmente sensibles.'
        )
    })

    # Control Humano
    evaluaciones.append({
        'criterio': 'Control Humano',
        'resultado': not resultado_analisis['automatiza_decisiones'],
        'observaciones': (
            'Hay intervención humana'
            if not resultado_analisis['automatiza_decisiones']
            else 'Proceso automatizado sin intervención clara.'
        )
    })

    # Autoría IA
    evaluaciones.append({
        'criterio': 'Autoría IA',
        'resultado': not resultado_analisis['sospecha_ia'],
        'observaciones': (
            'Código aparentemente escrito por humano'
            if not resultado_analisis['sospecha_ia']
            else 'Posible generación automática por IA. Revisión ética recomendada.'
        )
    })

    # Nuevos criterios

    # Documentación
    evaluaciones.append({
        'criterio': 'Documentación técnica',
        'resultado': resultado_analisis['incluye_documentacion'],
        'observaciones': (
            'Se encontraron docstrings o comentarios útiles.'
            if resultado_analisis['incluye_documentacion']
            else 'No se detectó documentación interna.'
        )
    })

    # Uso de modelos explicables
    evaluaciones.append({
        'criterio': 'Explicabilidad del modelo',
        'resultado': resultado_analisis['usa_modelos_explicables'],
        'observaciones': (
            'Se usan técnicas explicables como SHAP o árboles de decisión.'
            if resultado_analisis['usa_modelos_explicables']
            else 'No se detectan mecanismos de explicabilidad.'
        )
    })

    # Autonomía alta
    evaluaciones.append({
        'criterio': 'Autonomía del sistema',
        'resultado': not resultado_analisis['usa_autonomia_alta'],
        'observaciones': (
            'El sistema requiere intervención o validación.'
            if not resultado_analisis['usa_autonomia_alta']
            else 'Se detectó lógica autónoma de decisión.'
        )
    })

    # Licencia o uso libre
    evaluaciones.append({
        'criterio': 'Licencia de uso',
        'resultado': resultado_analisis['incluye_licencia'],
        'observaciones': (
            'Se declara tipo de licencia en el código.'
            if resultado_analisis['incluye_licencia']
            else 'No se encontró información de licencia.'
        )
    })

    # Consentimiento de datos
    evaluaciones.append({
        'criterio': 'Consentimiento de datos',
        'resultado': resultado_analisis['requiere_consentimiento'],
        'observaciones': (
            'Se hace referencia a consentimiento/autorización.'
            if resultado_analisis['requiere_consentimiento']
            else 'No se menciona consentimiento para uso de datos.'
        )
    })

    return evaluaciones
