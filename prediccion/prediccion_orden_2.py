import numpy as np


def prediccion_caracter_orden2(par, matriz, alfabeto):

    n = len(alfabeto)

    # Identificar los índices de los dos caracteres
    indices_alfabeto = {
        caracter: i for i, caracter in enumerate(alfabeto)
    }

    if len(par) != 2 or any(c not in indices_alfabeto for c in par):
        return []

    i = indices_alfabeto[par[0]]
    j = indices_alfabeto[par[1]]

    # Obtener la fila correspondiente al par
    fila = i * n + j
    probabilidades = matriz[fila]

    # Obtener los caracteres con probabilidad distinta de cero
    indices_validos = np.where(probabilidades > 0)[0]

    # Ordenar de mayor a menor probabilidad
    indices_ordenados = indices_validos[
        np.argsort(probabilidades[indices_validos])[::-1]
    ]

    # Seleccionar los dos más probables
    mejores = indices_ordenados[:2]

    return [
        (alfabeto[k], probabilidades[k])
        for k in mejores
    ]