import requests
from bs4 import BeautifulSoup   
import auxiliar as aa

url = 'https://seleciona.sefin.ro.gov.br/' 
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

cl = soup.select('.section-title')
sec = soup.find_all('section')
