# Server File
# Aidan Liljehorn
# CS 330
# Credit/Sources: Bek Brace & ProgrammingKnowledge on YouTube (Guiding the code that is presented here).

import socket
import twenty_questions_protocol
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 5477
ThreadCount = 0
clients = []


try:
    server.bind((host, port))
except socket.error as e:
    print(str(e))

print('Listening...')
server.listen(2)

def serverThread(client):
    # Server initiates and incorporates the protocol
    TQS = twenty_questions_protocol.TQP()
    while True:
        inputLn = client.recv(1024)

        # Server runs client input through the protocol to
        # receive the servers output back to the client based on the protocol
        outputLn = TQS.processInput(inputLn.decode())

        if outputLn.lower().startswith('reg'):
            split = outputLn.split()
            clients.append(split[1])

        # Based on the protocols response to the clients input, server sends the output response back to the client
        client.sendall(str.encode(outputLn))

    client.close()


while True:
    client, address = server.accept()
    clients.append(client)
    print('Client connected by', address)
    start_new_thread(serverThread, (client, ))
    ThreadCount += 1
    print('Thread Count: ', ThreadCount)
server.close()

'''
# Server initiates and incorporates the protocol
TQS = twenty_questions_protocol.TQP()

# Server receives inputs from the client
while True:
    inputLn = client.recv(1024)
    protocolInput = inputLn.decode()

# Server runs client input through the protocol to receive the servers output back to the client based on the protocol
    outputLn = TQS.processInput(protocolInput)

# Based on the protocols response to the clients input, server sends the output response back to the client
    outputLn = str.encode(outputLn)
    client.send(outputLn)
'''


'''
while True:
    TQS = twenty_questions_protocol.TQP()
    inputLn = ''
    outputLn = TQS.processInput()
    client_read = client.makefile()
    while client_read.readline() != '':
        input_read = inputLn.makefile()
        out = input_read.readline()
        server_send = str.encode(outputLn(out))
        client.send(server_send)
'''