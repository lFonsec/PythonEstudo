import csv
import time
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:/Users/lucas/Documents/Udemy Python/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url = 'https://www.paodeacucar.com/categoria/bebidas-alcoolicas/cervejas?' \
      'qt=12&ftr=facetSubShelf_ss%3A10360_Cervejas__sellType_s%3A1P&p=35&gt=grid'
browser.get(url)

SCROLL_PAUSE_TIME = 0.5  # tempo de espera para a pagina carregar

last_height = browser.execute_script("return document.body.scrollHeight")  # pega a altura da pagina

while True:

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll para baixo

    time.sleep(SCROLL_PAUSE_TIME)  # espera a pagina carregar

    new_height = browser.execute_script(
        "return document.body.scrollHeight")  # pega o novo tamanho da pagina e compara com o antigo
    if new_height == last_height:
        break
    last_height = new_height


data = datetime.datetime.now()
soup = BeautifulSoup(browser.page_source, 'html.parser')
product_card = soup.find_all('div', {"class": "product-cardstyles__CardStyled-sc-1uwpde0-0 bTCFJV cardstyles__Card-yvvqkp-0 grtyhB"})
nome_produto = []
preco_produto = []
filename = 'Scrapper Pao de Ac ' + str(data.day) + '_' + str(data.month) + '.csv'

with open(filename, 'w', encoding='windows-1252') as csvfile:
    fieldnames = ['Nome', 'Precos']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for valor in product_card:

        nome_produto = valor.find('a', {"class": "product-cardstyles__Link-sc-1uwpde0-9 bSQmwP hyperlinkstyles__Link-j02w35-0 hcByGl"}).contents
        # aux = valor.find('span', {"class": "buttonstyles__Text-sc-1mux0mx-2 iHGqzy"})  # pega o valor do botao
        aux2 = valor.find('span', {"class": "buttonstyles__Text-sc-1mux0mx-2 iHGqzy"})
        # checa_botao = str(aux)  # e muda pra string

        if aux2 is None:  # checa se botao ta indisponivel
            preco_produto = ['R$00,00']
        else:
            preco_produto = valor.find("div", {"class": "price-tag-normalstyle__LabelPrice-sc-1co9fex-0 lkWvql"}).contents

        writer.writerow({'Nome': nome_produto, 'Precos': preco_produto})

browser.close()

