from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get("https://www.paodeacucar.com/adega/secoes/6511/Cervejas")
soup = BeautifulSoup(response.text, "html.parser")
events = soup.find_all('div', {"class": "product-cardstyles__CardStyled-sc-1uwpde0-0"})
print(events)


house_events = []
for event in events:
    house_events = event.find('a', {"class": "product-cardstyles__Link-sc-1uwpde0-6 kJkixe hyperlinkstyles__Link-j02w35-0 cZAwm"})

"""   if genre_list.find(text='House'):
        title = event.find('h1', {'class' : 'title'}).a.text
        date = event.find('h1', {'class' : 'nicedate'}).text
        house_events.append((title, date))"""

print(house_events)
