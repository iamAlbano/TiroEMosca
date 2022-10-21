import functools
import tkinter as t
from menu import Menu
from tela import Tela
from singleplayer import Singleplayer
from multiplayer import Game
import tcp_cliente
import server
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

tela_singleplayer = []
tela_multiplayer = []

def singleplayer_game():
    tela.muda_tela(singleplayer)

def vs_cpu_game():
    tela.muda_tela(vs_cpu)

def multiplayer_game():
    tela.muda_tela(multiplayer)

def voltar_menu():
    tela.muda_tela(tela)

# opções que aparecem em cada tela da aplicação
singleplayer_options = [
    {'text': 'Escolha seu modo de jogo', 'type': 'label', 'column':0, 'row':1 },
    {'text': 'Jogar sozinho', 'type': 'button', 'column':0, 'row':2, 'action':singleplayer_game},
    {'text': 'VS CPU', 'type': 'button', 'column':0, 'row':3, 'action':vs_cpu_game },
]
multiplayer_options = [
    {'text': 'Multiplayer', 'type': 'label', 'column':0, 'row':0 },
    {'text': 'Iniciar jogo', 'type': 'button', 'column':0, 'row':1, 'action':multiplayer_game},
]


# aplicando opções as telas da aplicação
tela_singleplayer = Tela(root, 'SinglePlayer', singleplayer_options)
tela_multiplayer = Tela(root, 'Multiplayer', multiplayer_options)  

if __name__ == '__main__':

    root.geometry("400x400")
    
    menu = Menu(root, tela_singleplayer, tela_multiplayer)
    singleplayer = Singleplayer(menu, False)
    vs_cpu = Singleplayer(menu, True)
    multiplayer = Game(menu)
    menu.grid()

    root.mainloop()