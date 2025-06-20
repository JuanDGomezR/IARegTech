from abc import ABC, abstractmethod

class CertificadorIA(ABC):
    def __init__(self, sistema):
        self.sistema = sistema

    @abstractmethod
    def emitir_certificado(self) -> dict:
        pass
