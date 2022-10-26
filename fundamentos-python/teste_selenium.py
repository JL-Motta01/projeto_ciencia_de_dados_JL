import requests
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
import lxml

def exemplo_selenium ():
    navegador=webdriver.Firefox()
    navegador.get("https://www.google.com/?gws_rd=ssl")
    buscar=navegador.find_element (By.NAME, "q")
    buscar.send_keys("Unesp")
    sleep (3)
    buscar.send_keys(Keys.ENTER)


def deputados_carregar_mais ():
    '''Responsável por clicar no botão carregar mais e passar as informações carregadas para o BeautifulSoup'''
    navegador = webdriver.Firefox()
    navegador.get("https://www.camara.leg.br/noticias/ultimas?pagina=")
    sleep(3)
    cookie=navegador.find_element(By.CSS_SELECTOR,"#onetrust-accept-btn-handler")
    cookie.click()
    sleep(2)
    carregar_mais=WebDriverWait(navegador,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.general-container > section > div > div.load-more__wrapper > span")))
    for _ in range (12):
        print("carregar_mais")
        carregar_mais.click()
        sleep(2)
    bs=BeautifulSoup(navegador.page_source,"lxml")
    navegador.close()
    return bs

def extrair_infos():
    bs= deputados_carregar_mais()
    lista_de_tags_artigos = bs.find_all("article")
    for tag_article in lista_de_tags_artigos:
        titulo = tag_article.a.find("h2", attrs={"class":"articles-item__title"})
        link = tag_article.["href"]
        data= bs.find("div",attrs={"class":"articles-item__meta"}).find_all("span")[0].text
        tag= bs.find ("div",attrs={"class":"articles-item__meta"}).text
        print(titulo.text)
        print(link)
        print(data)
        print(tag)

def main ():
    #exemplo_selenium ()
    extrair_infos()




if __name__ == "__main__":
    main ()
