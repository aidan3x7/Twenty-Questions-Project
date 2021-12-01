# Server File
# Aidan Liljehorn
# CS 330
# Credit/Sources: Bek Brace & ProgrammingKnowledge on YouTube (Guiding the code that is presented here).

'''
import threading
import twenty_questions_protocol
'''

import socket

host = "127.0.0.1"
port = 10821

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
client, address = server.accept()
print(client, 'connected by', address)

while True:
    message = client.recv(1024)
    client.send(message)