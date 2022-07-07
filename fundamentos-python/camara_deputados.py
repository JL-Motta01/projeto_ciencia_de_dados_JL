from io import DEFAULT_BUFFER_SIZE
from urllib import parse
from urllib.request import urlopen
import urllib
import urllib.request #realizar requisição da página html
from tinydb import TinyDB,Query
from urllib.parse import urlparse #realizar parseamento do html
from bs4 import BeautifulSoup #importa o beautifulsoup para extrair as infos das tags
from pprint import pprint #organizar estéticamente os prints


DIR_LOCAL= "/home/labri_joaomotta/codigo/fundamentos-de-ciencias-de-dados/fundamentos-python/DB"

def acessar_pagina(url):
    """Analisa os noticias do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def paginas_com_url_noticias ():
    """Percorre as páginas onde ficam os links"""
    lista_url_noticias = []
    contador = 0
    while contador<70:
        dominio = "https://www.camara.leg.br/noticias/ultimas?pagina="
        dominio += str(contador)
        contador += 1
        lista_url_noticias.append(dominio)
    return lista_url_noticias

def coleta_link():
    """Coleta os links de cada página que contém noticias"""
    lista_links=[]
    for url in paginas_com_url_noticias():
        html = acessar_pagina(url)
        noticias = html.find_all("h3", class_=["g-chamada__titulo"] )
        for noticia in noticias:
            links = noticia.a["href"]
            lista_links.append(links)
    return lista_links

def coleta_conteudo():
    """Responsável por coletar título, parágrafo, Tags, atualização e data das noticias"""
    db = TinyDB(f"{DIR_LOCAL}/db_noticia.json", ensure_ascii=False)
    User = Query()
    for link in coleta_link():
        noticias = acessar_pagina(link)
        url = link
        publicado_em = noticias.find("p", class_="g-artigo__data-hora").text.split("-")
        atualizado_em = "NA"
        try:
            tags=noticias.find("span", class_="g-artigo__categoria").text
        except:
            tags="NA"
        titulo = noticias.find("h1", class_="g-artigo__titulo").text
        try:
            subtitulo =noticias.find("p", class_="g-artigo__descricao").text
        except:
            subtitulo="NA"
        try:
            lista_conteudo=[]
            paragrafos = noticias.find('div', class_="g-artigo__texto-principal").find_all(['p','h3','h2','h1'])
            for conteudo in paragrafos:
                if conteudo.name == 'h3' or conteudo.name == 'h2' or conteudo.name == 'h1':
                    texto = conteudo.text
                    texto = texto.upper()
                else:
                    texto = conteudo.text 
                lista_conteudo.append(texto)
        except:
            lista_conteudo= "NA"
        db_camara_dep = db.contains((User.titulo==titulo)&(User.data==publicado_em))
        if not db_camara_dep:
            print("não está na base")
            db.insert({
                "origem": "camara dos deputados",
                "classificado": "noticia",
                "data":publicado_em[0],
                "horario":publicado_em[1],
                "atualizado em":atualizado_em,
                "titulo":titulo,
                "subtitulo":subtitulo,
                "link":url,           
                "tags":tags,
                "conteudo":lista_conteudo,
            })
        else:
            print("está na base")


def main ():
    """Função principal"""
    coleta_conteudo()

if __name__ == "__main__":
    main()