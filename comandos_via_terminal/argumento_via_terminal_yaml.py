#python3 argumento_via_terminal_config.ini.py -n1 2 -n2 5 -o resultado.txt 
#https://docs.python.org/3/library/configparser.html.

import argparse
import sys
import yaml
def soma(number, other_number, output):
    result = number + other_number
    print(f'O resultado do soma é: {result}', file=output)
def subtracao(number, other_number, output):
    result = number - other_number
    print(f'O resultado do subtracao é: {result}', file=output)
if __name__ == '__main__':
    #print('As operações seguiram os seguintes critérios: 1 para soma, 2 para subracao')
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help='A number', default=1)
    parser.add_argument('-n2', type=int, help='Another number', default=1)
    parser.add_argument('-c', dest='config', type=argparse.FileType('r'), default=None, help='config file')
    parser.add_argument('-o', dest='output', type=argparse.FileType('w'), help='Output file', default=sys.stdout)
    
    args = parser.parse_args()

    if args.config:
        config = yaml.load(args.config, Loader=yaml.FullLoader)
        args.n1 = config['ARGUMENTS']['n1']
        args.n2 = config['ARGUMENTS']['n2']
    soma(args.n1, args.n2, args.output)
    subtracao(args.n1, args.n2, args.output)

    #pagina 69