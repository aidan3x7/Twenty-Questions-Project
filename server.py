# Server File
# Aidan Liljehorn
# CS 330
# Credit/Sources: https://codezup.com/socket-server-with-multiple-clients-model-multithreading-python/

import socket
import twenty_questions_protocol
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 5477
ThreadCount = 0
shared = dict()
shared['clients'] = []
shared['open_rooms'] = []
shared['closed_rooms'] = []


try:
    server.bind((host, port))
except socket.error as e:
    print(str(e))

print('Listening...')
server.listen(2)

def serverThread(client):
    # Server initiates and incorporates the protocol
    TQS = twenty_questions_protocol.TQP(client, user_room, user_room_index, word)
    while True:
        inputLn = client.recv(1024)

        # Server runs client input through the protocol to
        # receive the servers output back to the client based on the protocol
        outputLn = TQS.processInput(inputLn.decode())

        # Based on the protocols response to the clients input, server sends the output response back to the client
        client.sendall(str.encode(outputLn))

    print('Connection lost.')
    client.close()


while True:
    client, address = server.accept()
    user_room = ''
    user_room_index = ''
    word = ''
    print('Client connected by', address)
    start_new_thread(serverThread, (client, ))
    ThreadCount += 1
    print('Thread Count: ', ThreadCount)
server.close()
