#coding:utf-8
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

DIR_DADOS= "/media/hdvm10/bd/003/001/001/001/001-b"

def acessar_pagina(url):
    """Analisa os auditoria do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def paginas_com_url_auditoria ():
    """Percorre as páginas onde fical os links"""
    lista_url_auditoria = ["https://www.gov.br/secretariageral/pt-br/estrutura/secretaria_de_controle_interno/resultados",
    "https://www.gov.br/economia/pt-br/acesso-a-informacao/auditorias",
    ""
    ]
    return lista_url_auditoria

def coleta_conteudo():
    """Responsável por coletar título, parágrafo, Tags, atualização e data dos auditoria"""
    db = TinyDB(f"{DIR_DADOS}/govlatinamerica/brasil/govfederal/govbr/bd/db_auditoria.json", ensure_ascii=False)
    User = Query()
    for link in paginas_com_url_auditoria():
        auditoria = acessar_pagina(link)
        links_pdf = auditoria.find_all("a", class_="internal-link")
        print(links_pdf)
        for pdf in links_pdf:
            url = pdf["href"]
            titulo = pdf.text
            db_planalto = db.contains(User.titulo==titulo)
            if not db_planalto:
                print("não está na base")
                #wget.download(url, f"{DIR_LOCAL}/govlatinamerica/brasil/govfederal/govbr/bd/pdf_auditoria/")
                link_pdf = requests.get(url[:-5])
                local = f"{DIR_DADOS}/govlatinamerica/brasil/govfederal/govbr/bd/pdf_auditoria/"
                with open(f'{local}/{titulo}', "wb") as arq_pdf:
                    arq_pdf.write(link_pdf.content)
                db.insert({
                    "origem": "Presidência da República",
                    "classificado": "Auditorias",
                    "link":url, 
                    "titulo":titulo,
                })
            else:
                print("está na base")


def main ():
    """Função principal"""
    coleta_conteudo()

if __name__ == "__main__":
    main()