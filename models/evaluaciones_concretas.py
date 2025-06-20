from models.evaluacion import EvaluacionEtica

class EvaluacionTransparencia(EvaluacionEtica):
    def criterio(self):
        return self.sistema['nivel_intervencion_humana'] != 'Baja'

class EvaluacionDiscriminacion(EvaluacionEtica):
    def criterio(self):
        return not self.sistema['uso_datos_personales']

class EvaluacionControlHumano(EvaluacionEtica):
    def criterio(self):
        return self.sistema['nivel_intervencion_humana'] == 'Alta'
