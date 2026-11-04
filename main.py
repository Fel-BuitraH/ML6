from lector_y_procesador_texto.lector_libro import leer_libro
from lector_y_procesador_texto.procesador_texto import preparar_texto 
from estadistica.frecuencia_caracteres import contar_caracteres
from estadistica.histograma import graficar_frecuencias

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