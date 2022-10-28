import os
from time import sleep
from datetime import datetime

paths = ['python', 'javascript', 'pandas', 'numpy', 'mapasmentais', 'curso_data_science']

def git_comand(paths, comand):
    print(f"Rodando '{comand}' em pasta {paths}")
    os.system(f"cd {paths} && {comand}")

def git_status():
    for i in range(len(paths)):
        print(f"/{'_'*10}Status em: {paths[i].upper()}{'_'*10}/")
        git_comand(paths[i], 'git status')
        sleep(0.5)

def git_pull():
    for i in range(len(paths)):
        print(f"/{'_'*10}Pull em: {paths[i].upper()}{'_'*10}/")
        git_comand(paths[i], 'git pull')
        sleep(0.5)

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
    print("0 for 'ALL STATUS'\n9 for 'GIT PULL'\nDOUBLE NUMBER FOR PUSH\nNOFHING FOR QUIT")

if __name__ == '__main__':
    while True:
        welcome()
        option = input('Write your option: ')
        if option == '':
            break
        elif len(option[0:]) > 1:
            key = int(option[0])
            git_up(paths[key])
            sleep(1.5)
        elif option == '0':
            git_status()
        elif option == '9':
            git_pull()