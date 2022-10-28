import os
from time import sleep
from datetime import datetime

paths = ['Python', 'javascript', 'mapasmentais', 'curso_data_science']

def git_comand(paths, comand):
    print(f"Rodando '{comand}' em pasta {paths}")
    os.system(f"cd {paths} && {comand}")

def git_up(path):
    nome_da_maquina = os.uname()[1]
    data_e_hora_atuais = datetime.now()
    data_e_hora_atuais = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    
    os.system(f"cd {path} && git add . && git commit -m '{nome_da_maquina} em {data_e_hora_atuais}' && git push")


def welcome():
    for i in range(len(paths)):
        print(f'{i} for {paths[i].upper()}')
    print('\n')
    print('Concatene with comands below: \n')
    print("0 for 'ALL STATUS'\nDouble for push\nNofhing for quit\n9 for all pull")

if __name__ == '__main__':
    while True:
        welcome()
        option = input('Write your option: ')
        
        if option == '':
            break
        if len(option[0:]) > 1:
            key = int(option[0])
            git_up(paths[key])
            sleep(1.5)
        elif option == '0':
            for i in range(len(paths)):
                print(f'_____________{paths[i].upper()}_______________')
                git_comand(paths[i], 'git status')
                sleep(0.5)
        elif option == '9':
            for i in range(len(paths)):
                print(f'_____________Pull in: {paths[i].upper()}_______________')
                git_comand(paths[i], 'git pull')
                sleep(0.5)
            