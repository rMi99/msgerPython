import socket
import threading

import clients as clients

HOST = '127.0.0.1'
PORT = 9090

server = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clinets = []
nicknames = []

def brodcast(message):
    for client in clinets:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clinets.index(client)]}")
            brodcast(message)
        except:
            index = clinets.index(client)
            clients.close()
            nicknames = nicknames[index]
            nicknames.remove(nicknames)
            break



def recevice():
    while True:
        clinet, address = server.accept()
        print(f"Connected with {str(address)}!")

        clinet.send("NICK".encode('utf-8'))
        nickname = clinet.recv(1024)

        clients.append(clinet)

        print(f"Nickname of the client is {nickname}")
        brodcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(clinet,))
        thread.start()


print("Server Running")
recevice()



