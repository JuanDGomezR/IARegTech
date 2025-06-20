from abc import ABC, abstractmethod

class EstrategiaRiesgo(ABC):
    @abstractmethod
    def evaluar(self, sistema):
        pass

class RiesgoBasico(EstrategiaRiesgo):
    def evaluar(self, sistema):
        if sistema['nivel_intervencion_humana'] == 'Alta' and not sistema['uso_datos_personales']:
            return 'Bajo'
        return 'Medio'

class RiesgoModerado(EstrategiaRiesgo):
    def evaluar(self, sistema):
        if sistema['nivel_complejidad'] == 'Medio' or sistema['uso_datos_personales']:
            return 'Medio'
        return 'Bajo'

class RiesgoAlto(EstrategiaRiesgo):
    def evaluar(self, sistema):
        if sistema['nivel_complejidad'] == 'Alto' and sistema['uso_datos_personales']:
            return 'Alto'
        return 'Medio'
