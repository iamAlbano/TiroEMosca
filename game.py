# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro, Guilherme Albano, Dani"

import tkinter as t
import socket, sys
from threading import *

HOST = '127.0.0.1'  # endereço IP
PORT = 20000        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados

class Game(t.Frame):

  def __init__(self, parent):
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.socket.connect((HOST, PORT))
      self.tiros = 0
      self.moscas = 0
      self.tentativa = ''
      self.texto_recebido = ''
      try:
        t.Frame.__init__(self)

        recvThread = Thread(target=self.recebeMsg)
        recvThread.daemon = True
        recvThread.start()
        
        t.Label(self, text="Chutar número de 0 a 9: ").grid(column=0, row=0, padx=60, pady=5)
        self.tentativa = t.Entry(self, width=40)
        self.tentativa.insert(0,"Tentativa: ")
        self.tentativa.grid(column=0, row=1, padx=60, pady=10)
        btnSendMessage = t.Button(self, text="Send", width=20, command=self.enviarMensagem)
        btnSendMessage.grid(column=0, row=2,padx=10, pady=10)
        t.Label(self, text="Tiros: "+str(self.tiros)).grid(column=0, row=3, padx=60, pady=5)
        t.Label(self, text="Moscas: "+str(self.moscas)).grid(column=0, row=4, padx=60, pady=5)
      except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return

  def enviarMensagem(self):
      clientMessage = self.tentativa.get()
      self.socket.send(clientMessage.encode()) #texto.encode - converte a string para bytes

  def recebeMsg(self):
    while True:
      data = self.socket.recv(BUFFER_SIZE)
      self.texto_recebido = repr(data)
      texto_string = data.decode('utf-8')
      print('Recebido do servidor', self.texto_recebido)
      if (texto_string == 'GAME_OVER'):
          print('vai encerrar o socket cliente!')
          self.socket.close()

