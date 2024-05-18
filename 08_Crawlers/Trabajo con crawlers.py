from bs4 import BeautifulSoup

miDoc="""

    <html>
        <body>
            <p>Este es el primer párrafo</p>
            <p>Este es el segundo párrafo</p>

            <a>Es un vínculo<a>

        </body>
    </html>

"""
# extraer el documento
docFinal=BeautifulSoup(miDoc, "html.parser")

# buscar en el documento
for parrafo in docFinal.find_all("p"):

    # Imprimir el texto que encuentre
    print(parrafo.text) 

print(docFinal)