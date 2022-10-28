import PyPDF2

arquivo_pdf = open('27.10.2022.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(arquivo_pdf)
numero_paginas = pdf.getNumPages()
paginas = pdf.getPage(130)
paginas.extract_text()