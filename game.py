# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro, Guilherme Albano, Dani"

import json  
import tkinter as t
import socket, sys
from threading import Thread
from random import randint

HOST = '127.0.0.1'  # endereço IP
PORT = 20000        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados

class Game(t.Frame):

  def __init__(self, parent):
      super(Game, self).__init__()
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.socket.connect((HOST, PORT))
      self.tentativa = ''
      self.turno = None
      self.minha_sequencia = str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9))
      self.pacote = { "tentativa": "", "tiros": 0, "moscas": 0 }
      self.tiros = 0
      self.moscas = 0

      try:
        t.Frame.__init__(self)

        # componentes do layout
        sequencia_label = t.Label(self, text="A sua sequência é: "+self.minha_sequencia)
        adversario_label = t.Label(self, text="Seu adversário chutou: ")
        chute_label = t.Label(self, text="Chutar sequência de três números: ")
        tentativa = t.Entry(self, width=40)

        def enviarTentativa():
          clientMessage = tentativa.get()
          self.pacote = { "tentativa": clientMessage }
          data = json.dumps(self.pacote).encode('utf-8')
          self.socket.send(data) 
        
        def calcularTirosEMoscas(tentativa):
          numeros = list(tentativa)
          sequencia = list(self.minha_sequencia)
          quantidade_tiros = 0
          quantidade_moscas = 0
          tiros = []
          moscas = []
          for i, numero in enumerate(numeros):
            for j, valor in enumerate(sequencia):
              if numero == valor:
                 if i == j:
                  quantidade_moscas +=1
                  moscas.append(numero)
                  break
                 else: 
                  if numero not in moscas and numero not in tiros:
                    tiros.append(numero)
                    quantidade_tiros +=1

          enviarFeedback(quantidade_tiros, quantidade_moscas)
        
        def enviarFeedback(tiros, moscas):
          self.pacote = { "tiros":tiros, "moscas": moscas }
          data = json.dumps(self.pacote).encode('utf-8')
          self.socket.send(data) 

        btn_enviar = t.Button(self, text="Chutar", width=20, command=enviarTentativa)
        tiros_label = t.Label(self, text="Tiros: "+str(self.tiros))
        moscas_label =  t.Label(self, text="Moscas: "+str(self.moscas))

        aguardando = t.Label(self, text="Aguardando adversário...")

        def recebeMsg():
          while True:
            data = self.socket.recv(BUFFER_SIZE)
            pacote_recebido = json.loads(data)
            if 'turno' in pacote_recebido:
              self.turno = pacote_recebido['turno']
            if 'tentativa' in pacote_recebido:
              adversario_label.configure(text="Seu adversário chutou: "+pacote_recebido['tentativa'])
              calcularTirosEMoscas(pacote_recebido['tentativa'])
            if 'tiros' in pacote_recebido:
              self.tiros = pacote_recebido['tiros']
              tiros_label.configure(text="Tiros: "+str(self.tiros))
            if 'moscas' in pacote_recebido:
              self.moscas = pacote_recebido['moscas']
              moscas_label.configure(text="Moscas: "+str(self.moscas))

            if 'GAME_OVER' in pacote_recebido:
                print('vai encerrar o socket cliente!')
                self.socket.close()

        recvThread = Thread(target=recebeMsg)
        recvThread.daemon = True
        recvThread.start()
      
        sequencia_label.grid(column=0, row=0, padx=60, pady=5)
        adversario_label.grid(column=0, row=1, padx=60, pady=5)
        chute_label.grid(column=0, row=2, padx=60, pady=5)
        
        tentativa.insert(0,"")
        tentativa.grid(column=0, row=3, padx=60, pady=10)
        
        btn_enviar.grid(column=0, row=4,padx=10, pady=10)
        
        tiros_label.grid(column=0, row=6, padx=60, pady=5)
        moscas_label.grid(column=0, row=7, padx=60, pady=5)
          

      except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return

      

