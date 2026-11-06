import numpy as np
import string
from pathlib import Path


def texto_bayes_orden2(matriz, alfabeto, longitud=1000):

    letras = string.ascii_lowercase
    n = len(alfabeto)

    # Seleccionar dos caracteres iniciales
    indices = [
        i for i, caracter in enumerate(alfabeto)
        if caracter in letras
    ]

    iniciales = np.random.choice(indices, size=2)
    texto = ['t','h']

    # Generar los caracteres restantes
    for _ in range(longitud - 2):

        i = alfabeto.index(texto[-2])
        j = alfabeto.index(texto[-1])

        fila = i * n + j
        probabilidades = matriz[fila]

        # Comprobar que existan transiciones conocidas
        if probabilidades.sum() == 0:
            break

        siguiente = np.random.choice(
            n,
            p=probabilidades
        )

        texto.append(alfabeto[siguiente])

    texto_generado = ''.join(texto)

    # Guardar resultado
    ruta = Path("resultados/texto_bayes_orden2.txt")
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto_generado, encoding="utf-8")

    return texto_generado
