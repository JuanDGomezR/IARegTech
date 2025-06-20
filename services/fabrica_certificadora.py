from models.certificadores_concretos import CertificadorSalud, CertificadorEducacion, CertificadorGenerico

def obtener_certificador(sistema):
    sector = sistema['sector']
    if sector == 'Salud':
        return CertificadorSalud(sistema)
    elif sector == 'Educación':
        return CertificadorEducacion(sistema)
    else:
        return CertificadorGenerico(sistema)
