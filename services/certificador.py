def generar_certificacion(sistema_dict):
    riesgo = sistema_dict.get('riesgo', '').lower()

    if riesgo == 'alto':
        return {'nivel': 'Rechazado', 'obs': 'Uso riesgoso de IA con variables sensibles.'}
    elif riesgo == 'medio':
        return {'nivel': 'Condicionado', 'obs': 'Requiere revisión por decisiones automatizadas.'}
    elif riesgo == 'bajo':
        return {'nivel': 'Aprobado', 'obs': 'Sistema ético y con bajo riesgo.'}
    else:
        return {'nivel': 'Pendiente', 'obs': 'Riesgo no clasificado aún.'}
