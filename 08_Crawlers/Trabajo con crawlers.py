from bs4 import BeautifulSoup

import requests

from urllib.parse import urljoin

class PostCrawled():

    def __init__(self, titulo, emoticono, contenido, imagen):
        
        self.titulo=titulo
        self.emoticono=emoticono
        self.contenido=contenido
        self.imagen=imagen

class PostExtractor():

    def extraeInfo(self):

        urlBase="https://python.beispiel.programmierenlernen.io/"

        miDoc=requests.get(urlBase)

        # extraer el documento
        docFinal=BeautifulSoup(miDoc.text, "html.parser")

        posts=[]

        for card in docFinal.select(".card"):
            titulo=card.select(".card-title span")[1].text
            emoticono=card.select_one(".emoji").text
            contenido=card.select_one(".card-text").text
            imagen=urljoin(urlBase,card.select_one("img").attrs["src"])

            crawled=PostCrawled(titulo,emoticono, contenido, imagen)
            posts.append(crawled)

        return posts

unPost=PostExtractor()

listaPosts=unPost.extraeInfo()

for elPost in listaPosts:

    print(elPost.emoticono)
    print(elPost.titulo)
    print(elPost.contenido)
    print(elPost.imagen)
    print()

# print(listaPosts)