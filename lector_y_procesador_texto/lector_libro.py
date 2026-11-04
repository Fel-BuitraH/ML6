
import zipfile
from html.parser import HTMLParser


class ExtractorDeTexto(HTMLParser):
    """
    Extrae el texto visible de un documento HTML/XHTML,
    ignorando el contenido de las etiquetas script y style.
    """

    def __init__(self):
        super().__init__()
        self.fragmentos = []
        self.ignorando = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.ignorando = True

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.ignorando = False

    def handle_data(self, data):
        if not self.ignorando:
            self.fragmentos.append(data)

    def obtener_texto(self):
        return "".join(self.fragmentos)


def leer_libro(ruta_epub):
    """
    Lee un archivo EPUB y extrae el texto de sus documentos
    HTML/XHTML.

    Parámetros:
        ruta_epub (str): Ruta del archivo EPUB.

    Retorna:
        str: Texto extraído del libro.
    """

    textos = []

    with zipfile.ZipFile(ruta_epub, "r") as epub:

        for nombre in epub.namelist():

            if nombre.lower().endswith((".xhtml", ".html", ".htm")):

                contenido = epub.read(nombre).decode(
                    "utf-8", errors="replace"
                )

                extractor = ExtractorDeTexto()
                extractor.feed(contenido)

                textos.append(extractor.obtener_texto())

    return "\n".join(textos)
