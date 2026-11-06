import numpy as np
import string 

def texto_bayes(matriz, alfabeto, longitud=200):

    letras = string.ascii_lowercase

    # Índices correspondientes a letras minúsculas
    indices = [
        i for i, caracter in enumerate(alfabeto)
        if caracter in letras
    ]

    # Seleccionar carácter inicial
    indice = np.random.choice(indices)
    texto = [alfabeto[indice]]

    for _ in range(longitud - 1):

        probabilidades = matriz[indice]

        indice = np.random.choice(
            len(alfabeto),
            p=probabilidades
        )

        texto.append(alfabeto[indice])

    return ''.join(texto)