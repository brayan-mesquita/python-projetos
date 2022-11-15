import requests
from bs4 import BeautifulSoup



url = 'https://seleciona.sefin.ro.gov.br/'

response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
page_title = page.title.string

cl = page.select('.section-title')

len(cl)