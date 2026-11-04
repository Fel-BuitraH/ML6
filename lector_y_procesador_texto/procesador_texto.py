
import string


def preparar_texto(texto):
    """
    Prepara el texto para el análisis de caracteres.
    Conserva letras inglesas, espacios y puntuación.
    """

    texto = texto.lower()

    caracteres_validos = string.ascii_lowercase + string.punctuation + string.whitespace
    caracteres_ignorados = "=+ #[]%"

    texto = "".join(
    caracter for caracter in texto
    if caracter in caracteres_validos
    and caracter not in caracteres_ignorados
)

    return texto
