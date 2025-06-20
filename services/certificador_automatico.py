def emitir_certificacion(riesgo):
    if riesgo == 'Bajo':
        return {'nivel': 'Aprobado', 'obs': 'Sistema ético y con bajo riesgo.'}
    elif riesgo == 'Medio':
        return {'nivel': 'Condicionado', 'obs': 'Requiere revisión por decisiones automatizadas.'}
    else:
        return {'nivel': 'Rechazado', 'obs': 'Uso riesgoso de IA con variables sensibles.'}
