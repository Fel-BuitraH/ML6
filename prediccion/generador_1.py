import numpy as np
import string
from collections import Counter
from pathlib import Path

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
    texto_generado = ''.join(texto)

    # Generar los caracteres restantes
    for _ in range(longitud - 1):

        indice = np.random.choice(
            len(alfabeto),
            p=probabilidades
        )

        texto.append(alfabeto[indice])

    # Guardar el texto generado
    ruta = Path("resultados/texto_punto_1.txt")
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto_generado, encoding="utf-8")

    return texto_generado