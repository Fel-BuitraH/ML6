
import string



def preparar_texto(texto):

    texto = texto.lower()

    caracteres_validos = string.ascii_lowercase + string.punctuation + string.whitespace
    caracteres_ignorados = "=+#[]%"

    texto = "".join(
    caracter for caracter in texto
    if caracter in caracteres_validos
    and caracter not in caracteres_ignorados
)

    return texto
