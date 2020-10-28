from mostrar_datos.carga_datos import carga_dic
import numpy as np


def result(cedula, ruta_encuesta):
    encuestados = carga_dic(ruta_encuesta)
    lista_num = encuestados[cedula]['respuestas']
    total = np.sum(lista_num)
    return total