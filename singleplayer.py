# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro, Guilherme Albano, Dani"

import json  
import tkinter as t
from random import randint

class Singleplayer(t.Frame):

  def __init__(self, parent):
      super(Singleplayer, self).__init__()
      self.tentativa = ''
      self.sequencia = str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9))
      self.tiros = 0
      self.moscas = 0
      self.parent = parent
      msg = t.Label(self, text="Aguardando adversário")
      self.layout = msg

      try:
        t.Frame.__init__(self)

        mensagem = t.Label(self, text="Chutar sequência de três números: ")
        tentativa = t.Entry(self, width=40)

        def chutar_sequencia():
          calcular_Tiros_E_Moscas()

        # componentes do layout
        btn_enviar = t.Button(self, text="Chutar", width=20, command=chutar_sequencia)
        tiros_label = t.Label(self, text="Tiros: "+str(self.tiros))
        moscas_label =  t.Label(self, text="Moscas: "+str(self.moscas))
      
        class jogo(t.Frame):
          def __init__(self):
            t.Frame.__init__(self)
            mensagem.grid(column=0, row=2, padx=60, pady=5)
            tentativa.insert(0,"")
            tentativa.grid(column=0, row=3, padx=60, pady=10)
            btn_enviar.grid(column=0, row=4,padx=10, pady=10)
            tiros_label.grid(column=0, row=6, padx=60, pady=5)
            moscas_label.grid(column=0, row=7, padx=60, pady=5)
        
        def atualiza_layout():
          self.layout.grid_forget()
          self.layout = jogo()
          self.layout.grid(column=0, row=0, padx=20, pady=20)

        atualiza_layout()

        def inicia_novo_jogo():
          self.sequencia = str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9))
          self.tiros = 0
          self.moscas = 0
          tiros_label.configure(text="Tiros: "+str(self.tiros))
          moscas_label.configure(text="Moscas: "+str(self.moscas))
          mensagem.configure(text="Chutar sequência de três números: ")
          btn_enviar.configure(text="Chutar", command=chutar_sequencia)

        def fim_jogo():
          mensagem.configure(text="Você ganhou!")
          btn_enviar.configure(text="Novo jogo", command=inicia_novo_jogo)
        
        def calcular_Tiros_E_Moscas():
          numeros = list(tentativa.get())
          sequencia = list(self.sequencia)
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
          
          if quantidade_moscas == 3:
            fim_jogo()
          self.moscas = quantidade_moscas
          self.tiros = quantidade_tiros
          tiros_label.configure(text="Tiros: "+str(self.tiros))
          moscas_label.configure(text="Moscas: "+str(self.moscas))

      except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return
    

      

