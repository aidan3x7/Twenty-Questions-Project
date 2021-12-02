# Server File
# Aidan Liljehorn
# CS 330
# Credit/Sources: Bek Brace & ProgrammingKnowledge on YouTube (Guiding the code that is presented here).

'''
import threading
import twenty_questions_protocol
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
