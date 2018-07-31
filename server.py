
 
from socket import *
import time
 
# Cria o nome do host
meuHost = ''

minhaPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
 
# Vincula o servidor ao número de porto
sockobj.bind((meuHost, minhaPort))
 
# O socket começa a esperar por clientes limitando a 
# 5 conexões por vez
sockobj.listen(5)
 
 
while True:

    conexão, endereço = sockobj.accept()
    print('Server conectado por', endereço)
     
    while True:
        # Recebe data enviada pelo cliente
        data = conexão.recv(1024)

        if not data: break
 
        # O servidor manda de volta uma resposta
        conexão.send(b'Eco=>' + data)
     
    # Fecha a conexão criada depois de responder o
    # cliente
    conexão.close()