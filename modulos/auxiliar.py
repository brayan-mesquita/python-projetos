def tipo(*args):
    for variavel in args:
        print(f'Tipo{type(variavel)}')
        
def valor(*args):
    for variavel in args:
        print(f'Valor{type(variavel)}')
def linha():
    print('_'*100)

def abrir(local):
    with open(local) as arquivo:
      return arquivo.read()

def exportar(variavel):
    with open(f'{variavel}.txt', 'wr') as arquivo:
        arquivo.write(b)

#sys.path.insert (0, '/Users/brayan/Documents/projetos/projetos_python/modulos')