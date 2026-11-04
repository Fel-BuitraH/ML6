import string
import numpy as np
import pandas as pd

caracteres_validos = string.ascii_lowercase + string.punctuation + string.whitespace
caracteres_ignorados = "=+#[]%"

def matriz_conteos(texto):

    #Matriz de conteos de pares de caracteres en el texto.

    alfabeto = sorted(set(caracteres_validos) - set(caracteres_ignorados))
    
    indices_alfabeto =  {caracter: i for i, caracter in enumerate(alfabeto)} 

    matriz_alfabeto = np.zeros((len(alfabeto), len(alfabeto)), dtype=int)

    for actual, siguiente in zip(texto, texto[1:]):
        i = indices_alfabeto[actual]
        j = indices_alfabeto[siguiente]

        matriz_alfabeto[i, j] += 1

    return matriz_alfabeto, alfabeto


def normalizar_matriz(matriz_conteos):

    #Matriz de probabilidades normalizada a partir de la matriz de conteos.

    sumas_filas = matriz_conteos.sum(axis=1, keepdims=True)

    matriz_probabilidades = np.divide(
        matriz_conteos,
        sumas_filas,
        out=np.zeros_like(matriz_conteos, dtype=float),
        where=sumas_filas != 0
    )

    return matriz_probabilidades


def matriz_csv(matriz, alfabeto, ruta):
    
    tabla = pd.DataFrame(matriz, index=alfabeto, columns=alfabeto)

    tabla.to_csv(ruta, encoding="utf-8", index_label="Actual")