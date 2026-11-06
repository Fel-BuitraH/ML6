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

def bayes_prueba_matriz(matriz, a, b):
    
    N = matriz.sum()

    # Probabilidades
    p_a = matriz[a, :].sum() / N
    p_b = matriz[:, b].sum() / N

    # Probabilidades condicionales
    p_b_a = matriz[a, b] / matriz[a, :].sum()
    p_a_b = matriz[a, b] / matriz[:, b].sum()


    izquierda = p_b_a * p_a
    derecha = p_a_b * p_b

    return izquierda, derecha

def bayes_prueba_total(matriz):

    N = matriz.sum()

    # Marginales
    marginal_a = matriz.sum(axis=1)
    marginal_b = matriz.sum(axis=0)

    # Productos de probabilidades
    a1 = matriz / N
    a2 = matriz / N

    # Comparación de todos los pares
    validos = (marginal_a[:, None] > 0) & (marginal_b[None, :] > 0)

    return a1[validos], a2[validos]
