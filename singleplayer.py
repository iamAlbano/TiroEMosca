# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro, Guilherme Albano, Dani"

import json  
import tkinter as t
from random import randint, choice

class Singleplayer(t.Frame):

  def __init__(self, parent, vs_cpu=False):
      super(Singleplayer, self).__init__()
      self.parent = parent
      self.tentativa = ''
      self.minha_sequencia = str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9)) # sequencia que a cpu deve acertar
      self.tiros = 0
      self.moscas = 0

      self.sequencia_cpu = str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9)) # sequencia que o jogador deve acertar
      self.tentativa_cpu_aux = [randint(0, 9), randint(0, 9), randint(0, 9)]
      self.memoria_tentativa_cpu = [self.tentativa_cpu_aux[0], self.tentativa_cpu_aux[1], self.tentativa_cpu_aux[2]]
      self.posicao_atual = 0
      self.quantidade_chutes = 0
      self.chutes_cpu = [ list(range(0,10)), list(range(0,10)), list(range(0,10)) ]
      self.array_tiros_cpu = []
      self.memoria_cpu = { 'tiros': 0, 'moscas': 0 }
      self.tiros_cpu = 0
      self.moscas_cpu = 0

      msg = t.Label(self, text="Aguardando adversário")
      self.layout = msg

      try:
        t.Frame.__init__(self)

        sequencia_label = t.Label(self, text="A sua sequência é: "+self.minha_sequencia)
        adversario_label = t.Label(self, text="A CPU chutou: ")
        mensagem = t.Label(self, text="Chutar sequência de três números: ")
        tentativa = t.Entry(self, width=40)

        def cpu_chuta_sequencia():
          chute_cpu = str(self.tentativa_cpu_aux[0])+str(self.tentativa_cpu_aux[1])+str(self.tentativa_cpu_aux[2])
          adversario_label.configure(text="A CPU chutou: "+chute_cpu)
          quantidade_tiros, quantidade_moscas = calcular_Tiros_E_Moscas(chute_cpu, self.minha_sequencia)
          self.moscas_cpu = quantidade_moscas
          self.tiros_cpu = quantidade_tiros
          if quantidade_moscas == 3:
            fim_jogo()

          else:
            if(  self.memoria_cpu['moscas'] > quantidade_moscas ):
              self.tentativa_cpu_aux[self.posicao_atual] = self.memoria_tentativa_cpu[self.posicao_atual]
              self.posicao_atual +=1

            
            self.memoria_tentativa_cpu[self.posicao_atual] = self.tentativa_cpu_aux[self.posicao_atual]
            if( len(self.chutes_cpu[self.posicao_atual]) > 0 ):
              self.tentativa_cpu_aux[self.posicao_atual] = choice(self.chutes_cpu[self.posicao_atual])
              self.chutes_cpu[self.posicao_atual].remove(self.tentativa_cpu_aux[self.posicao_atual])
            else:
              self.posicao_atual +=1
            self.memoria_cpu = { 'tiros': self.tiros_cpu, 'moscas': self.moscas_cpu }
            self.quantidade_chutes +=1

        def chutar_sequencia():
          quantidade_tiros, quantidade_moscas = calcular_Tiros_E_Moscas(tentativa.get(), self.sequencia_cpu)
          self.moscas = quantidade_moscas
          self.tiros = quantidade_tiros
          tiros_label.configure(text="Tiros: "+str(self.tiros))
          moscas_label.configure(text="Moscas: "+str(self.moscas))
          if quantidade_moscas == 3:
            fim_jogo()
          
          if vs_cpu:
            cpu_chuta_sequencia()
            

        # componentes do layout
        btn_enviar = t.Button(self, text="Chutar", width=20, command=chutar_sequencia)
        tiros_label = t.Label(self, text="Tiros: "+str(self.tiros))
        moscas_label =  t.Label(self, text="Moscas: "+str(self.moscas))
      
        class jogo(t.Frame):
          def __init__(self):
            t.Frame.__init__(self)
            if vs_cpu:
              sequencia_label.grid(column=0, row=0, padx=60, pady=5)
              adversario_label.grid(column=0, row=1, padx=60, pady=5)
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

        def reinicia_cpu():
          self.minha_sequencia = str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9))
          sequencia_label.configure(text="A sua sequência é: "+self.minha_sequencia)
          self.tentativa_cpu_aux = [randint(0, 9), randint(0, 9), randint(0, 9)]
          self.memoria_tentativa_cpu = [self.tentativa_cpu_aux[0], self.tentativa_cpu_aux[1], self.tentativa_cpu_aux[2]]
          self.posicao_atual = 0
          self.quantidade_chutes = 0
          self.chutes_cpu = [ list(range(0,10)), list(range(0,10)), list(range(0,10)) ]
          self.array_tiros_cpu = []
          self.memoria_cpu['tiros'] = 0
          self.memoria_cpu['moscas'] = 0 
          self.tiros_cpu = 0
          self.moscas_cpu = 0

        def inicia_novo_jogo():
          self.sequencia_cpu = str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9))
          self.tiros = 0
          self.moscas = 0

          if vs_cpu:
            reinicia_cpu()

          tiros_label.configure(text="Tiros: "+str(self.tiros))
          moscas_label.configure(text="Moscas: "+str(self.moscas))
          mensagem.configure(text="Chutar sequência de três números: ")
          btn_enviar.configure(text="Chutar", command=chutar_sequencia)

        def fim_jogo():
          if self.moscas == 3:
            mensagem.configure(text="Você ganhou!")
          else:
            mensagem.configure(text="A CPU venceu...")
          btn_enviar.configure(text="Novo jogo", command=inicia_novo_jogo)
        
        def calcular_Tiros_E_Moscas(tentativa, sequencia):
          numeros = list(tentativa)
          sequencia = list(sequencia)
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
          
          return quantidade_tiros, quantidade_moscas

      except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return
    

      

