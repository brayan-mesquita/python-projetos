def tipo(*args):
    for variavel in args:
        print(f'Tipo{type(variavel)}')
        
def valor(*args):
    for variavel in args:
        print(f'Valor{type(variavel)}')
def linha():
    print('_'*100)

def exportar(valor):
    arquivo = 'valor_exportado.txt'
    with open(f'arquivo.txt', 'wr') as arquivo:
        arquivo.write(b)


