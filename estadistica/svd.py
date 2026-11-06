import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def descomposicion_svd(matriz, nombre, ruta):

    U, S, VT = np.linalg.svd(matriz)

    plt.figure(figsize=(8, 5))
    plt.plot(S, marker='o')
    plt.xlabel("Índice del valor singular")
    plt.ylabel("Valor singular")
    plt.title(f"Descomposición SVD: {nombre}")
    plt.grid()

    Path(ruta).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    plt.close()

    return U, S, VT