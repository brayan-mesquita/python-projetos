import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
import PyPDF2

url = 'https://diof.ro.gov.br/'
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
page_title = page.title.string

def procurar_links_com_pdf():
    links_a = []
    for link in page.find_all('a'):
        links_a.append(link.get('href'))
    return [pdf for pdf in links_a if 'pdf' in pdf ]
a = procurar_links_com_pdf()
print(a)

def criar_dicionario(lista):
    dicionario = dict()
    TRA = '-'
    for i in lista:
        if TRA.join(i[-14:-4].split('.')) in dicionario:
            dicionario[f"{TRA.join(i[-14:-4].split('.'))}-s"] = i
            continue
        dicionario[TRA.join(i[-14:-4].split('.'))] = i
    return dicionario
d = criar_dicionario(procurar_links_com_pdf())
print(d.keys())
print('26-10-2022' in d)
len(d)


dicionario = criar_dicionario(procurar_links_com_pdf())
dicionario['28-10-2022']
for i in dicionario.keys():
    print(i)






#========ABRINDO ARQUIVOS======#
import PyPDF2
file_url = links_pdf[0]
file = f'{links_pdf[0][-14:-4]}.pdf'
request.urlretrieve(file_url , file )
arquivo_pdf = open('27.10.2022.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(arquivo_pdf)
numero_paginas = pdf.getNumPages()
numero_paginas

#-----LEITURA DIOF

arquivo_pdf = open('27.10.2022.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(arquivo_pdf)
numero_paginas = pdf.getNumPages()
paginas = pdf.getPage(130)
paginas.extract_text()





#===========GERENCIAR HORAS E DATA==============#
#data_e_hora_atuais = datetime.now()
#data_e_hora_atuais = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

#===========CRIAR DIRETORIOS==============#
from pathlib import Path
p = Path()
p.absolute()
web_scraping = p / 'web_scraping'
sub_pasta = web_scraping / 'sub_pasta'
sub_pasta.mkdir()
#transformando data, splitando separadores
data = '10.10.2022'
nova_pasta = p / '-'.join(data.split('.'))
#criando pasta e arquivos
lista_de_datas = ['10-10-2022', '11-10-2022']
def criar_diretorios_e_arquivos(a_criar):
    for name in a_criar:
        pasta = p / 'web_scraping'/ 'sub_pasta' / f'{name}'
        pasta.mkdir()
        arquivo = pasta / f'{name}.txt'
        arquivo.touch()
        with arquivo.open('a+') as text_file:
            text_file.write(f'Arquivo nome: {name}')
#criar_diretorios_e_arquivos(lista_de_datas)

def criar_diretorios():
    for pasta in links_pdf:
        dia = pasta[0][-14:-4]
        nova_pasta = path / dia
        nova_pasta.mkdir()

#===========DONWLOAD==============#
from urllib import request
file_url = links_pdf[0]
file = f'{links_pdf[0][-14:-4]}.pdf'
request.urlretrieve(file_url , file )