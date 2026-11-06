import numpy as np
import string
from collections import Counter


def texto_punto_1(textos, alfabeto, longitud=200):

    # Obtener frecuencias individuales
    conteo = Counter(textos)

    frecuencias = np.array([
        conteo[caracter] for caracter in alfabeto
    ])

    # Normalizar frecuencias
    probabilidades = frecuencias / frecuencias.sum()

    # Seleccionar una letra inicial
    letras = string.ascii_lowercase

    indices = [
        i for i, caracter in enumerate(alfabeto)
        if caracter in letras
    ]

    indice = np.random.choice(indices)
    texto = [alfabeto[indice]]

    # Generar los caracteres restantes
    for _ in range(longitud - 1):

        indice = np.random.choice(
            len(alfabeto),
            p=probabilidades
        )

        texto.append(alfabeto[indice])

    return ''.join(texto)