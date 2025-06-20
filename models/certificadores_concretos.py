from models.certificador import CertificadorIA

class CertificadorSalud(CertificadorIA):
    def emitir_certificado(self):
        if self.sistema['riesgo'] == 'Bajo':
            nivel = 'Aprobado'
        elif self.sistema['riesgo'] == 'Medio':
            nivel = 'Condicionado'
        else:
            nivel = 'Rechazado'
        return {'nivel': nivel, 'obs': 'Certificación emitida para sector salud.'}

class CertificadorEducacion(CertificadorIA):
    def emitir_certificado(self):
        if self.sistema['nivel_complejidad'] == 'Alto':
            return {'nivel': 'Condicionado', 'obs': 'Sistema muy complejo, requiere revisión adicional.'}
        return {'nivel': 'Aprobado', 'obs': 'Certificación emitida para educación.'}

class CertificadorGenerico(CertificadorIA):
    def emitir_certificado(self):
        return {'nivel': 'Condicionado', 'obs': 'Sistema evaluado con criterios generales.'}
