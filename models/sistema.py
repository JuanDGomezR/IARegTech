from extensions import mysql

class SistemaIA:
    def __init__(self, nombre, sector, descripcion, nivel_complejidad,
                 uso_datos_personales, tipo_aprendizaje, nivel_intervencion_humana):
        self.nombre = nombre
        self.sector = sector
        self.descripcion = descripcion
        self.nivel_complejidad = nivel_complejidad
        self.uso_datos_personales = uso_datos_personales
        self.tipo_aprendizaje = tipo_aprendizaje
        self.nivel_intervencion_humana = nivel_intervencion_humana
        self.id = None  # Se asignará después de guardar

    def guardar(self):
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO sistemas_ia 
            (nombre, sector, descripcion, nivel_complejidad,
             uso_datos_personales, tipo_aprendizaje, nivel_intervencion_humana)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            self.nombre,
            self.sector,
            self.descripcion,
            self.nivel_complejidad,
            self.uso_datos_personales,
            self.tipo_aprendizaje,
            self.nivel_intervencion_humana
        ))
        mysql.connection.commit()
        self.id = cur.lastrowid
        cur.close()

    @staticmethod
    def obtener(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM sistemas_ia WHERE id = %s", (id,))
        row = cur.fetchone()
        cur.close()

        if row:
            sistema = SistemaIA(
                nombre=row[1],
                sector=row[2],
                descripcion=row[3],
                nivel_complejidad=row[4],
                uso_datos_personales=row[5],
                tipo_aprendizaje=row[6],
                nivel_intervencion_humana=row[7]
            )
            sistema.id = row[0]
            return sistema
        else:
            return None
