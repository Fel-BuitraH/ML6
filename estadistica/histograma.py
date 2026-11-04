
import matplotlib.pyplot as plt


def graficar_frecuencias(frecuencias_1, frecuencias_2=None,
                         nombre_1="Libro 1", nombre_2="Libro 2"):
    
    # Obtener todos los caracteres presentes en los libros.
    caracteres = set(frecuencias_1)

    if frecuencias_2 is not None:
        caracteres.update(frecuencias_2)

    # Ordenar los caracteres según su frecuencia total.
    caracteres = sorted(
        caracteres,
        key=lambda c: (
            frecuencias_1.get(c, 0)
            + (frecuencias_2.get(c, 0) if frecuencias_2 else 0)
        ),
        reverse=True
    )

    posiciones = list(range(len(caracteres)))

    valores_1 = [frecuencias_1.get(c, 0) for c in caracteres]

    etiquetas = [repr(c) for c in caracteres]

    plt.figure(figsize=(12, 6))

    if frecuencias_2 is None:

        plt.bar(posiciones, valores_1, label=nombre_1)

    else:

        valores_2 = [frecuencias_2.get(c, 0) for c in caracteres]

        ancho = 0.4

        posiciones_1 = [p - ancho / 2 for p in posiciones]
        posiciones_2 = [p + ancho / 2 for p in posiciones]

        plt.bar(posiciones_1, valores_1, width=ancho, label=nombre_1)
        plt.bar(posiciones_2, valores_2, width=ancho, label=nombre_2)

    plt.xticks(posiciones, etiquetas)
    plt.xlabel("Caracteres")
    plt.ylabel("Frecuencia")
    plt.title("Frecuencia de caracteres")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()

    # Guardar la gráfica.
    plt.savefig("resultados/frecuencia_caracteres.png", dpi=300)

    plt.show()
    plt.close()