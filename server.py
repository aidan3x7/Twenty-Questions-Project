# Server File
# Aidan Liljehorn
# CS 330
# Credit/Sources: Bek Brace & ProgrammingKnowledge on YouTube (Guiding the code that is presented here).

'''
import threading
'''

import socket
import twenty_questions_protocol

host = "127.0.0.1"
port = 10821

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
client, address = server.accept()
print(client, 'connected by', address)

# Server initiates and incorporates the protocol
TQS = twenty_questions_protocol.TQP()

# Server receives inputs from the client
while True:
    inputLn = client.recv(1024)
    inputLn = inputLn.decode()

# Server runs client input through the protocol to receive the servers output back to the client based on the protocol
    outputLn = TQS.processInput(inputLn)

# Based on the protocols response to the clients input, server sends the output response back to the client
    outputLn = str.encode(outputLn)
    client.send(outputLn)

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