from services.estrategias_riesgo.estrategias import RiesgoBasico, RiesgoModerado, RiesgoAlto
from extensions import mysql

class ClasificadorRiesgo:
    def __init__(self, sistema):
        self.sistema = sistema
        self.estrategia = self.seleccionar_estrategia()

    def seleccionar_estrategia(self):
        if self.sistema['nivel_complejidad'] == 'Bajo':
            return RiesgoBasico()
        elif self.sistema['nivel_complejidad'] == 'Medio':
            return RiesgoModerado()
        else:
            return RiesgoAlto()

    def clasificar(self):
        nivel = self.estrategia.evaluar(self.sistema)
        cur = mysql.connection.cursor()
        cur.execute("UPDATE sistemas_ia SET riesgo = %s WHERE id = %s", (nivel, self.sistema['id']))
        mysql.connection.commit()
        cur.close()
        return nivel
