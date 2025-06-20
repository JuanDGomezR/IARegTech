from services.fabrica_certificadora import obtener_certificador
from extensions import mysql

def certificar_sistema(sistema_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sistemas_ia WHERE id = %s", (sistema_id,))
    data = cur.fetchone()
    keys = [desc[0] for desc in cur.description]
    sistema = dict(zip(keys, data))
    cur.close()

    certificador = obtener_certificador(sistema)
    resultado = certificador.emitir_certificado()

    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO certificados (sistema_id, nivel_aprobacion, observaciones)
        VALUES (%s, %s, %s)
    """, (sistema['id'], resultado['nivel'], resultado['obs']))
    cur.execute("UPDATE sistemas_ia SET estado_certificacion = %s WHERE id = %s",
                (resultado['nivel'], sistema['id']))
    mysql.connection.commit()
    cur.close()

    return resultado
