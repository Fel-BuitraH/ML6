import readchar
import numpy as np
from lector_y_procesador_texto.lector_libro import leer_libro
from lector_y_procesador_texto.procesador_texto import preparar_texto 
from estadistica.frecuencia_caracteres import contar_caracteres
from estadistica.histograma import graficar_frecuencias
from prediccion.training_orden_1 import matriz_conteos,normalizar_matriz, matriz_csv
from prediccion.prediccion_orden_1 import prediccion_caracter
from prediccion.bayes_orden_1 import texto_bayes_orden_1, bayes_prueba_matriz, bayes_prueba_total
from prediccion.generador_1 import texto_punto_1
from estadistica.svd import descomposicion_svd


ruta_libro1= "libros/la_republica.3.epub"
ruta_libro2 = "libros/el_retrato_de_dorian.3.epub"
ruta_libro3 = "libros/Crime_and_Punishment.3.epub"
ruta_libro4 = "libros/Pride_and_Prejudice.3.epub"
ruta_libro5 = "libros/The_Great_Gatsby.3.epub"

texto1 = leer_libro(ruta_libro1)
texto1_preparado = preparar_texto(texto1)

texto2 = leer_libro(ruta_libro2)
texto2_preparado = preparar_texto(texto2)

texto3 = leer_libro(ruta_libro3)
texto3_preparado = preparar_texto(texto3)

texto4 = leer_libro(ruta_libro4)
texto4_preparado = preparar_texto(texto4)

texto5 = leer_libro(ruta_libro5)
texto5_preparado = preparar_texto(texto5)

frecuencias1 = contar_caracteres(texto1_preparado)
frecuencias2 = contar_caracteres(texto2_preparado)
frecuencias3 = contar_caracteres(texto3_preparado)
frecuencias4 = contar_caracteres(texto4_preparado)
frecuencias5 = contar_caracteres(texto5_preparado)

graficar_frecuencias( frecuencias1,frecuencias2, 
                     nombre_1="La República", nombre_2="El retrato de Dorian Gray")



# Construir matrices de conteos
conteo_1, alfabeto = matriz_conteos(texto1_preparado)
conteo_2, _ = matriz_conteos(texto2_preparado)
conteo_3, _ = matriz_conteos(texto3_preparado)
conteo_4, _ = matriz_conteos(texto4_preparado)
conteo_5, _ = matriz_conteos(texto5_preparado)

conteo_total = conteo_1 + conteo_2 + conteo_3 + conteo_4 + conteo_5

# Obtener matriz de probabilidades
probabilidades= normalizar_matriz(conteo_total)


# Diccionario para identificar las posiciones
indices = {caracter: i for i, caracter in enumerate(alfabeto)}

## -----------------------------------------------------
## PUNTO 1.
## -----------------------------------------------------

#Guardar matrices en archivos CSV 
matriz_csv(conteo_total, alfabeto, "resultados/matriz_conteos_total.csv")
matriz_csv(probabilidades, alfabeto, "resultados/matriz_probabilidades_total.csv")

## -----------------------------------------------------
## PUNTO 2.
## -----------------------------------------------------

print("Escribe dos caracteres:")

for _ in range(2):

    caracter = readchar.readkey().lower()

    sugerencias = prediccion_caracter(caracter, probabilidades, alfabeto)

    print(caracter)
    print("Sugerencias:")

    for siguiente, probabilidad in sugerencias:
        print(f"{repr(siguiente):8} | {probabilidad:.4%}")


## -----------------------------------------------------
## PUNTO 3
## -----------------------------------------------------

texto_generado_bayes = texto_bayes_orden_1(probabilidades, alfabeto, longitud=200)

print("\nTexto generado usando Bayes guardado en 'resultados/texto_bayes_orden1.txt':")
textos = texto1_preparado + texto2_preparado

texto_generado_aleatorio = texto_punto_1(textos, alfabeto, longitud=200)

print("\nTexto aleatorio, tarea 1 guardado en 'resultados/texto_punto_1.txt':")

##Punto 4: Comprobación de Bayes

#Unicamente transiciones validas.
transiciones_validas = np.where((conteo_total.sum(axis=1) > 0) &(conteo_total.sum(axis=0) > 0))[0]
a, b = np.random.choice(transiciones_validas, size = 2, replace =True)

L1, L2 = bayes_prueba_matriz(conteo_total, a , b)

#Prueba aleatoria de Bayes para 2 caracteres aleatorios
print(f"\nComprobación de Bayes para los caracteres '{alfabeto[a]}' y '{alfabeto[b]}':")
print("P(B|A) * P(A):", L1)
print("P(A|B) * P(B):", L2)
print("¿Se cumple Bayes?", np.isclose(L1, L2, atol=1e-10))

#Prueba aleatoria de Bayes para toda la matriz alfxalf

a1, a2 = bayes_prueba_total(conteo_total)
print("\nComprobación de Bayes en toda la matriz alfabeto x alfabeto:")
print(f"Máxima diferencia: {np.max(np.abs(a1 - a2)):.8f}")
print("¿Se cumple Bayes en toda la matriz?", np.allclose(a1, a2))

##Punto 5. Descomposición SVD 

#Svd alfabeto*alfabeto
U_alf, S_alf, VT_alf = descomposicion_svd(conteo_total, "Matriz alfabeto * alfabeto", "resultados/svd_alfabeto.png")
#Svd probabilidades

U_prob, S_prob, VT_prob = descomposicion_svd(probabilidades, "Matriz probabilidades", "resultados/svd_probabilidades.png")



###EXTRAS

from prediccion.training_orden_2 import matriz_conteos_orden2, normalizar_matriz_orden2
from prediccion.bayes_orden_2 import texto_bayes_orden2

textos_entrenamiento = [
    texto1_preparado,
    texto2_preparado,
    texto3_preparado,
    texto4_preparado,
    texto5_preparado
]

conteo_orden2 = matriz_conteos_orden2(textos_entrenamiento, alfabeto)

probabilidades_orden2 = normalizar_matriz_orden2(conteo_orden2)

texto_generado = texto_bayes_orden2(
    probabilidades_orden2,
    alfabeto,
    longitud=1000
)

print("\nTexto generado (segundo orden), guardado en 'resultados/texto_bayes_orden2.txt':")