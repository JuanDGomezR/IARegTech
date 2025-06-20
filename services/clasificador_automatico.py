def clasificar_riesgo(resultado_analisis):
    if resultado_analisis['usa_ia']:
        if resultado_analisis['automatiza_decisiones'] and resultado_analisis['usa_variables_sensibles']:
            return 'Alto'
        elif resultado_analisis['automatiza_decisiones']:
            return 'Medio'
        else:
            return 'Bajo'
    return 'Bajo'
