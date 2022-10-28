import argparse
def soma(number, other_number):
    result = number + other_number
    print(f'O resultado do soma é: {result}')
def subtracao(number, other_number):
    result = number - other_number
    print(f'O resultado do subtracao é: {result}')
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help='A number', default=1)
    parser.add_argument('-n2', type=int, help='Another number', default=1)
    parser.add_argument('-o', type=int, help='Another number')
    args = parser.parse_args()
    operacao = ''
    if not args.o:
        print('As operações seguiram os seguintes critérios: 1 para soma, 2 para subracao')
        operacao = input('')
    if operacao == '1' or args.o == 1:
        soma(args.n1, args.n2)
    if operacao == '2' or args.o == 2:
        subtracao(args.n1, args.n2)