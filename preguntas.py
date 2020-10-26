from mostrar_datos.carga_datos import carga_dic


def preguntar(ruta_encuesta, ruta_preguntas):
    encuestados = carga_dic(ruta_encuesta)
    preguntas = carga_dic(ruta_preguntas)
    for pregunta in preguntas:
        print(pregunta)
        for respuestas in preguntas[pregunta]:
            print(respuestas)
