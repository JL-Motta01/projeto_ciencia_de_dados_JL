from urllib import parse
from urllib.request import urlopen
import urllib
import urllib.request #realizar requisição da página html
import os #para especificar o caminho do download
import requests
import csv
from urllib.parse import urlparse #realizar parseamento do html
from bs4 import BeautifulSoup #importa o beautifulsoup para extrair as infos das tags


DIR_LOCAL= "/home/labri_joaomotta/codigo"


def acessar_pagina(url):
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def pagina_coleta ():
    """Percorre as páginas onde fical os links"""
    Paginas = ["https://direitodacomunicacao.com/br/estrategia-de-governo-digital-no-periodo-de-2020-a-2022/", 
               "https://2017-2021.state.gov/the-clean-network/index.html",
               "https://jornal.usp.br/atualidades/implantacao-de-5g-e-oportunidade-do-brasil-avancar-em-areas-como-agricultura-saude-e-industria/",
               "https://www.camara.leg.br/noticias/730178-ministerio-da-defesa-defende-previsao-de-rede-privativa-do-governo-no-edital-do-5g/"]
    return Paginas

def coleta_conteudo():
    corpo_do_texto = []
    for link in pagina_coleta ():
        url = acessar_pagina(link)
        titulo1= url.find_all("h1")
        titulo2= url.find_all("h1")
        texto = url.find_all("p")
        for t in titulo1:
            corpo_do_texto.append(t.text.strip("\n"))
        for t in titulo2:
            corpo_do_texto.append(t.text.strip("\n"))
        for t in texto:
            corpo_do_texto.append(t.text.strip("\n"))
    print(corpo_do_texto)



def main ():
    """Função principal"""
    coleta_conteudo()

if __name__ == "__main__":
    main()