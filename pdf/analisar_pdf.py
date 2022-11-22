import PyPDF2
import tabula as tb


#pypdf2
arquivo_pdf = open('01-11-2022.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(arquivo_pdf)
numero_paginas = pdf.getNumPages()
paginas = pdf.getPage(1).extractText()
get = pdf.getPage(3)

dicionario = {}
for i in range(10):
    dicionario[i] = pdf.getPage(i).extract_text()
print(dicionario[1])

#tabula
tb.environment_info()
lista_tabelas = tb.read_pdf('01-11-2022.pdf', pages ='2-3')
lista_tabelas.convert_into(lista_tabelas, output_path)


def tipoenome(variavel):
    print(f'''Tem o type {type(variavel)}\nTem o tamanho {len(variavel)}''')
    print(f'''Possui extruturas {dir(variavel)}''')

