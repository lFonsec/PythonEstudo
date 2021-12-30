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

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


data = datetime.datetime.now()
soup = BeautifulSoup(browser.page_source, 'html.parser')
product_card = soup.find_all('div', {"class": "product-cardstyles__CardStyled-sc-1uwpde0-0 bTCFJV cardstyles__Card-yvvqkp-0 grtyhB"})
nome_produto = []
preco_produto = []
filename = 'Scrapper Pao de Aç ' + str(data.day) + '_' + str(data.month) + '.csv'

with open(filename, 'w', encoding='latin-1') as csvfile:
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

