import PyPDF2
import tabula as tb


#pypdf2
arquivo_pdf = open('01-11-2022.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(arquivo_pdf)
numero_paginas = pdf.getNumPages()
paginas = pdf.getPage(1).extractText()
len(paginas)


dicionario = {}
for i in range(100):
    dicionario[i] = pdf.getPage(i).extract_text()
dicionario[99]

#tabula
tb.environment_info()
lista_tabelas = tb.read_pdf('01-11-2022.pdf', pages = 'all')
type(lista_tabelas)
pg_4 = lista_tabelas[4]
print(pg_4)

