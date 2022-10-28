import requests
from bs4 import BeautifulSoup

#requests
url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)

#status code 200, 404 etc
response.status_code
#bs4
page = BeautifulSoup(response.text, 'html.parser')

page.title.string#nome da pagina

#======= procurar elementos======
h2, h3 = page.find_all('h2'), page.find_all('h3')
type(h3)#bs4.element.ResultSet

#extrair texto de todos h3
section = []
h3_chars = page.find('h3', attrs={'id': 'chars'})
for element in h3_chars.next_elements:
    if element.name == 'h3':
        break
    section.append(element.string or '')
result = ''.join(section)
result#resultado de texto sem html, uma verdadeira bagunca he

#======= adicionando elementos======
h3[-1].append(' Adicionando mais conteudo')
h3[-1]