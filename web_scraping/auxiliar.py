def tipo(*args):
    for variavel in args:
        print(f'Tipo{type(variavel)}')
        
def valor(*args):
    for variavel in args:
        print(f'Valor{type(variavel)}')
def linha():
    print('_'*100)

def exportar(variavel):
    with open(f'{variavel}.txt', 'wr') as arquivo:
        arquivo.write(b)


        