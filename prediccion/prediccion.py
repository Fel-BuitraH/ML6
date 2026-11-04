
import numpy as np


def prediccion_caracter(caracter, matriz_probabilidades, alfabeto):

    if caracter not in alfabeto:
        raise ValueError("El carácter no pertenece al alfabeto.")

    # Obtener la fila correspondiente al carácter actual
    indice = alfabeto.index(caracter)
    probabilidades = matriz_probabilidades[indice]

    # Comprobar que existan transiciones
    if probabilidades.sum() == 0:
        return []

    # Obtener los índices de las dos probabilidades mayores
    indices = np.argsort(probabilidades)[::-1]

    # Conservar únicamente las dos mayores probabilidades no nulas
    mejores = [
        i for i in indices
        if probabilidades[i] > 0
    ][:2]

    return [
        (alfabeto[i], probabilidades[i])
        for i in mejores
    ]
