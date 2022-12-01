import requests
from bs4 import BeautifulSoup   



url = 'https://seleciona.sefin.ro.gov.br/' 
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())

cl = soup.select('.section-title')
sec = soup.find_all('section')
sec


def linha():
    print('_'*100)