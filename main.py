import functools
import tkinter as t
from menu import Menu
from tela import Tela
from game import Game
import tcp_cliente
import tcp_server
import sys
import subprocess
import socket
from threading import Thread

root = t.Tk()
tela = Menu(root)
game_status = 'menu' # status atual do jogo
HOST = '127.0.0.1'  # endereço IP
PORT = 20000        # Porta utilizada pelo servidor

# inicializando telas da aplicaçao
singleplayer = []
multiplayer = []
config = []
hosting = []
game = []

def host_game():
    game_status = 'hosting'
    tela.muda_tela(hosting)
    start_host()

def start_host():
    # subprocess.call("tcp_server.py", shell=True)
    exec(open("tcp_server.py").read())

def enter_game():
    tela.muda_tela(game)

def voltar_menu():
    tela.muda_tela(tela)

# opções que aparecem em cada tela da aplicação
singleplayer_options = [
    {'text': 'Escolha seu modo de jogo', 'type': 'label', 'column':0, 'row':1 },
    {'text': 'Jogar sozinho', 'type': 'button', 'column':0, 'row':2, 'action':tcp_cliente.main },
    {'text': 'VS CPU', 'type': 'button', 'column':0, 'row':3, 'action':tcp_cliente.main },
]
multiplayer_options = [
    {'text': 'Escolha sua conexão', 'type': 'label', 'column':0, 'row':1 },
    {'text': 'HOST', 'type': 'button', 'column':0, 'row':2, 'action':host_game},
    {'text': 'CLIENT', 'type': 'button', 'column':0, 'row':3, 'action':enter_game},
]

hosting_options = [
    {'text': "Host criado no IP e porta:"+str(HOST)+":"+str(PORT), 'type': 'label', 'column':0, 'row':1 },
    {'text': 'Cancelar', 'type': 'button', 'column':0, 'row':2, 'action':voltar_menu},
]

config_options = [
    {'text': 'HOST', 'type': 'entry', 'column':0, 'row':1, 'action':enter_game},
    {'text': 'Porta', 'type': 'entry', 'column':0, 'row':2, 'action':enter_game},
    {'text': 'Salvar', 'type': 'button', 'column':0, 'row':3, 'action':enter_game},
]
# aplicando opções as telas da aplicação
singleplayer = Tela(root, 'SinglePlayer', singleplayer_options)
multiplayer = Tela(root, 'Multiplayer', multiplayer_options)  
config = Tela(root, 'Configurações', config_options) 
hosting = Tela(root, "Aguardando adversário", hosting_options)
game = Game(root)

if __name__ == '__main__':

    root.geometry("400x400")
    
    tela = Menu(root, singleplayer, multiplayer, config)
    tela.grid()

    root.mainloop()