import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service('C:/Users/lucas/Documents/Udemy Python/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url = 'https://www.paodeacucar.com/adega/secoes/6511/Cervejas?default_filters=%7B%22isRoot%22%3Atrue%2C%22filterId%22%3A%22categoria%22%2C%22filterValue%22%3A%22cervejas%22%7D%3B&sort=price%252Brev'
browser.get(url)


lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while match is False:
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True

soup = BeautifulSoup(browser.page_source, 'html.parser')
product_card = soup.find_all('div', {"class": "product-cardstyles__InnerContainer-sc-1uwpde0-4 ggdQez"})
nome_produto = []
preco_produto = []

aux = 0

for event in product_card:
    nome_produto = event.find('a', {"class": "product-cardstyles__Link-sc-1uwpde0-6 kJkixe hyperlinkstyles__Link-j02w35-0 cZAwm"}).contents
    print(nome_produto)

for valor in product_card:
    aux = valor.find('span', {"class": "buttonstyles__Text-sc-1mux0mx-1 jBMxTB"}).string #pega o valor do botao
    checa_botao = str(aux) #e muda pra string
    try:
        aux2 = valor.find('div', {"class": "seal-sale-box-divided__Label2-pf7r6x-2 bPAXAk"}).string
    except AttributeError:
        aux2 = 1
    checa_sale = str(aux2)
    if checa_botao == "Indisponível": #checa se botao ta indisponivel
        preco_produto = ['######']
    elif checa_sale == "A unid. sai por " and checa_botao != "Indisponível":
        preco_produto = valor.fin("div", {"class": "seal-sale-box-divided__Value-pf7r6x-3 bgtGEw"}).contents
    else:
        preco_produto = valor.find("div", {"class": "price-tag-normal__LabelPrice-fb5itg-0 iFihUZ"}).contents
    print(preco_produto)

browser.close()


#Arrumar a ocasião de promoção diferente "Sale Box"