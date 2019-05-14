import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Rio_Grande_do_Sul_por_data_de_cria%C3%A7%C3%A3o'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})
df = pd.read_html(str(table))[0]

cities = df[1]

print(cities.count)