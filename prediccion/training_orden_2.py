import string
import numpy as np

caracteres_validos = (
    string.ascii_lowercase
    + string.punctuation
    + string.whitespace
)

caracteres_ignorados = "=+#[]%"

alfabeto = sorted(
    set(caracteres_validos) - set(caracteres_ignorados)
)

def matriz_conteos_orden2(textos, alfabeto):

    # Diccionario para identificar los índices de los caracteres
    indices_alfabeto = {
        caracter: i for i, caracter in enumerate(alfabeto)
    }

    n = len(alfabeto)

    # Matriz: pares de caracteres x caracteres siguientes
    matriz = np.zeros((n**2, n), dtype=int)

    # Recorrer los cinco textos preparados
    for texto in textos:

        for i in range(len(texto) - 2):

            c1 = texto[i]
            c2 = texto[i + 1]
            siguiente = texto[i + 2]

            # Índice correspondiente al par de caracteres
            fila = (
                indices_alfabeto[c1] * n
                + indices_alfabeto[c2]
            )

            columna = indices_alfabeto[siguiente]

            matriz[fila, columna] += 1

    return matriz


def normalizar_matriz_orden2(matriz):

    sumas = matriz.sum(axis=1, keepdims=True)

    probabilidades = np.divide(
        matriz,
        sumas,
        out=np.zeros_like(matriz, dtype=float),
        where=sumas != 0
    )

    return probabilidades