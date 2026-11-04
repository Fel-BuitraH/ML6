import readchar
from lector_y_procesador_texto.lector_libro import leer_libro
from lector_y_procesador_texto.procesador_texto import preparar_texto 
from estadistica.frecuencia_caracteres import contar_caracteres
from estadistica.histograma import graficar_frecuencias
from prediccion.training import matriz_conteos,normalizar_matriz, matriz_csv
from prediccion.prediccion import prediccion_caracter

ruta_libro1= "libros/la_republica.3.epub"
ruta_libro2 = "libros/el_retrato_de_dorian.3.epub"

texto1 = leer_libro(ruta_libro1)
texto1_preparado = preparar_texto(texto1)

texto2 = leer_libro(ruta_libro2)
texto2_preparado = preparar_texto(texto2)

frecuencias1 = contar_caracteres(texto1_preparado)
frecuencias2 = contar_caracteres(texto2_preparado)

graficar_frecuencias( frecuencias1,frecuencias2, 
                     nombre_1="La República", nombre_2="El retrato de Dorian Gray")



# Construir matrices de conteos
conteo_1, alfabeto = matriz_conteos(texto1_preparado)
conteo_2, _ = matriz_conteos(texto2_preparado)

conteo_total = conteo_1 + conteo_2

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

print("Escribe un carácter (ESC para salir):")

while True:

    caracter = readchar.readkey().lower()

    if caracter == readchar.key.ESC:
        break

    sugerencias = prediccion_caracter(caracter, probabilidades, alfabeto)

    print(caracter)
    print("Sugerencias:")

    for siguiente, probabilidad in sugerencias:
        print(f"{repr(siguiente):8} | {probabilidad:.4%}")
