import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
import PyPDF2


#requests
url = 'https://diof.ro.gov.br/'
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
page_title = page.title.string

def search_all_links_pdf():
    links_a = []
    for link in page.find_all('a'):
        links_a.append(link.get('href'))
    return [pdf for pdf in links_a if 'pdf' in pdf ]

links_pdf = search_all_links_pdf()
def imprime_datas():
    for doe in links_pdf:
        print(doe[-14:-4])#DOE-24.10.2022
imprime_datas()

links_pdf[0]


#========ABRINDO ARQUIVOS======#
file_url = links_pdf[0]
file = f'{links_pdf[0][-14:-4]}.pdf'
request.urlretrieve(file_url , file )
arquivo_pdf = open('27.10.2022.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(arquivo_pdf)
numero_paginas = pdf.getNumPages()
numero_paginas
#===========GERENCIAR HORAS E DATA==============#
#data_e_hora_atuais = datetime.now()
#data_e_hora_atuais = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

#===========CRIAR DIRETORIOS==============#
p = Path()

#transformando data, splitando separadores
data = '10.10.2022'
nova_pasta = p / '-'.join(data.split('.'))

#criando pasta e arquivos
for i in range(2):
    pasta = p / f'pasta_numer_{i}'
    pasta.mkdir()
    arquivo = pasta / f'arquivo{i}.txt'
    arquivo.touch()
    with arquivo.open('a+') as text_file:
        text_file.write(f'Arquivo numero{i}')

def criar_diretorios():
    for pasta in links_pdf:
        dia = pasta[0][-14:-4]
        nova_pasta = path / dia
        nova_pasta.mkdir()

criar_diretorios()

type(dia)






#===========DONWLOAD==============#
from urllib import request
file_url = links_pdf[0]
file = f'{links_pdf[0][-14:-4]}.pdf'
request.urlretrieve(file_url , file )