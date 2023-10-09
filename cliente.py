import requests
from rich import print
import os

SERVIDOR_URL = 'http://127.0.0.1:5555'

def enviar_mensagem(nome):
    msg = input("Digite sua mensagem: ")
    msg = f'<{nome}> {msg}'
    resposta = requests.post(f'{SERVIDOR_URL}/enviar', json={'mensagem': msg})
    print(resposta.json()['status'])

def receber_mensagens(nome):
    resposta = requests.get(f'{SERVIDOR_URL}/receber')
    mensagens = resposta.json()['mensagens']
    print("Mensagens recebidas:")
    for msg in mensagens:
        if msg.find(nome) == -1:
            print(f'- [bold green]{msg}[/bold green]')
        else:
            print(f'- [bold blue]{msg}[/bold blue]')
        

if __name__ == '__main__':
    username = input("Digite seu nome: ")
    while True:
        print("1. Enviar mensagem")
        print("2. Receber mensagens")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            os.system('cls')
            enviar_mensagem(username)
        elif escolha == '2':
            os.system('cls')
            receber_mensagens(username)
        elif escolha == '0':
            os.system('cls')
            exit()
        else:
            print("Opção inválida.")
