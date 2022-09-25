# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro, Guilherme Albano, Dani"

import socket, sys


HOST = '127.0.0.1'  # endereço IP
PORT = 20000        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados


def main(HOST, PORT): 
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while(True):       
                texto = input("Digite o texto a ser enviado ao servidor:\n")
                s.send(texto.encode()) #texto.encode - converte a string para bytes
                data = s.recv(BUFFER_SIZE)
                texto_recebido = repr(data) #converte de bytes para um formato "printável"
                print('Recebido do servidor', texto_recebido)
                texto_string = data.decode('utf-8') #converte os bytes em string
                if (texto_string == 'bye'):
                    print('vai encerrar o socket cliente!')
                    s.close()
                    break
    except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return


if __name__ == "__main__":   
    main()