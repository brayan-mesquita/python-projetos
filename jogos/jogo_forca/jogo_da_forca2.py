import random
def carrega_palavra_secreta():
    arquivos_de_letras = open('palavras.txt', 'r')
    lista_palavras = []
    for palavra in arquivos_de_letras:
        lista_palavras.append(palavra.strip())
    indice_secreto = random.randint(0, (len(lista_palavras)))
    return lista_palavras[indice_secreto]

def percorrer_palavra(palavra='padrao'):
    lista = []
    for letra in palavra:
        lista.append(letra)
    lista_oculta = ['-' for x in lista]    
    palavra_secreta = lista
    return palavra_secreta, lista_oculta

def verifica_chute(palavra_secreta, lista_oculta, chute):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            lista_oculta[posicao] = chute
        posicao += 1
    if chute in palavra_secreta:
        return True
    else:
        return False

palavra_secreta, lista_oculta = percorrer_palavra(carrega_palavra_secreta())
erro = 0
acerto = 0
while True:
    chute = input('Digite o chute: ')
    if chute in lista_oculta:
        print(f'Ops! voce ja digitou {chute}')
        continue
    erro_ou_acerto = verifica_chute(palavra_secreta, lista_oculta, chute)
    if erro_ou_acerto:
        print(f'A letra {chute} esta na palavra secreta')
        print(lista_oculta)
        acerto += 1
        if palavra_secreta == lista_oculta:
            palavra_oculta = ''
            print(f'Voce acertou, a palavra é {palavra_oculta.join(palavra_secreta)}')
            break
    elif erro_ou_acerto == False:
        erro += 1
        print(f'A letra {chute} não está na palavra secreta\nVoce tem {int((1.5*len(palavra_secreta))-erro)} chances')
        if erro >= (1.5*len(palavra_secreta)):
            print('voce perdeu!')
            break