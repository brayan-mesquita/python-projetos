import PyPDF2
import tabula as tb
import warnings
warnings.filterwarnings("ignore") 

#pypdf2
arquivo_pdf = open('01-11-2022.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(arquivo_pdf)
numero_paginas = pdf.getNumPages()
paginas = pdf.getPage(130)
paginas.extract_text()

#tabula
tb.environment_info()
lista_tabelas = tb.read_pdf('01-11-2022.pdf', pages = 'all')
type(lista_tabelas)
pg_4 = lista_tabelas[4]
print(pg_4)

