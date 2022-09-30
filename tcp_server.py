# -*- coding: utf-8 -*-
__author__ =  "Filipe Ribeiro, Guilherme Albano, Dani"

import json  
import socket, sys
from threading import Thread

BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados

players = []

def on_new_client(clientsocket,addr):
    # avisa os jogadores sobre ínicio do jogo e define o primeiro a jogar
    novo_jogo = json.dumps({ "turno": clientsocket is not players[0]["client"]  if 'adversario' else 'jogador'})
    clientsocket.send(novo_jogo.encode('utf-8'))
    print("enviado: ", novo_jogo)
    while True:
        try:
            data = clientsocket.recv(BUFFER_SIZE)
            if not data:
                break
            texto_recebido = json.loads(data)
            print('recebido do cliente {} na porta {}: {}'.format(addr[0], addr[1],texto_recebido))
            
            # envia informação aos jogadores          
            for player in players:
                if player["client"] is not clientsocket:
                    player["client"].send(data)
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
            while True:
                print("Host criado no IP e porta: ", HOST,":",PORT)
                clientsocket, addr = server_socket.accept()
                players.append( { "client":clientsocket, "addr":addr} )
                if len(players) == 2:
                    for player in players:
                        print('Conectado ao cliente no endereço:', player["addr"])
                        t = Thread(target=on_new_client, args=( player["client"], player["addr"]) )
                        t.start()   
                    
    except Exception as error:
        print("Erro na execução do servidor")
        print(error)        
        return             



if __name__ == "__main__":   
    main()