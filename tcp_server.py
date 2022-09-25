# -*- coding: utf-8 -*-
__author__ =  "Filipe Ribeiro, Guilherme Albano, Dani"

import socket, sys
from threading import Thread

BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados

def on_new_client(clientsocket,addr):
    while True:
        try:
            data = clientsocket.recv(BUFFER_SIZE)
            if not data:
                break
            texto_recebido = data.decode('utf-8') # converte os bytes em string
            print('recebido do cliente {} na porta {}: {}'.format(addr[0], addr[1],texto_recebido))
            # envia o mesmo texto ao cliente           
            clientsocket.send(data)
            if (texto_recebido == 'bye'):
                print('vai encerrar o socket do cliente {} !'.format(addr[0]))
                clientsocket.close() 
                return 
        except Exception as error:
            print("Erro na conexão com o cliente")
            return


def main( HOST = '127.0.0.1', PORT = 20000 ):
    try:
        # AF_INET: indica o protocolo IPv4. SOCK_STREAM: tipo de socket para TCP,
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            server_socket.listen(0)
            print("Host criado no IP e porta: ", HOST,":",PORT)
            while True:
                clientsocket, addr = server_socket.accept()
                print('Conectado ao cliente no endereço:', addr)
                t = Thread(target=on_new_client, args=(clientsocket,addr))
                t.start()   
    except Exception as error:
        print("Erro na execução do servidor")
        print(error)        
        return             



if __name__ == "__main__":   
    main()