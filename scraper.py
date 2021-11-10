from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s=Service('C:/Users/lucas/Documents/Udemy Python/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url='https://www.paodeacucar.com/adega/secoes/6511/Cervejas'
browser.get(url)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
soup = BeautifulSoup(browser.page_source, 'html.parser')
events = soup.find_all('div', {"class": "product-cardstyles__CardStyled-sc-1uwpde0-0"})
nome_produto = []
preco_produto = []

for event in events:
    nome_produto = event.find('a', attrs={"class": "product-cardstyles__Link-sc-1uwpde0-6 kJkixe hyperlinkstyles__Link-j02w35-0 cZAwm"}).contents
print(nome_produto)

"""time.sleep(3)

for event in events:
    preco_produto = event.find("div", attrs={"class": "price-tag-normal__LabelPrice-fb5itg-0 iFihUZ"}).contents
print(preco_produto)
"""