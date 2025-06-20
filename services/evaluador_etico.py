from models.evaluaciones_concretas import (
    EvaluacionTransparencia,
    EvaluacionDiscriminacion,
    EvaluacionControlHumano
)
from extensions import mysql

def ejecutar_evaluaciones(sistema_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sistemas_ia WHERE id = %s", (sistema_id,))
    data = cur.fetchone()
    keys = [desc[0] for desc in cur.description]
    sistema_dict = dict(zip(keys, data))
    cur.close()

    evaluaciones = [
        EvaluacionTransparencia(sistema_dict),
        EvaluacionDiscriminacion(sistema_dict),
        EvaluacionControlHumano(sistema_dict)
    ]

    resultados = []
    cur = mysql.connection.cursor()
    for evaluacion in evaluaciones:
        resultado = evaluacion.evaluar()
        resultados.append(resultado)
        cur.execute("""
            INSERT INTO evaluaciones_eticas (sistema_id, criterio, resultado, observaciones)
            VALUES (%s, %s, %s, %s)
        """, (sistema_id, resultado['criterio'], resultado['resultado'], resultado['observaciones']))
    mysql.connection.commit()
    cur.close()
    return resultados
