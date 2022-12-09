import requests
from bs4 import BeautifulSoup   

class Verifica_sefin():
    def alteracao(self):
        response = requests.get('https://seleciona.sefin.ro.gov.br/')
        soup = BeautifulSoup(response.text, 'html.parser')
        id_services = soup.find('section', attrs={'id':'services'})
        if len(id_services) > 3:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Verifica_sefin().alteracao())
