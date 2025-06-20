from abc import ABC, abstractmethod

class EvaluacionEtica(ABC):
    def __init__(self, sistema):
        self.sistema = sistema

    def evaluar(self):
        resultado = self.criterio()
        observaciones = self.comentario(resultado)
        return {
            'criterio': self.__class__.__name__.replace('Evaluacion', ''),
            'resultado': resultado,
            'observaciones': observaciones,
            'sistema_id': self.sistema['id']
        }

    @abstractmethod
    def criterio(self):
        pass

    def comentario(self, resultado):
        return "Cumple adecuadamente." if resultado else "Debe mejorarse para cumplir criterios éticos."
