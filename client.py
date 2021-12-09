# Client File
# Aidan Liljehorn
# CS 330
# Credit/Sources: https://codezup.com/socket-server-with-multiple-clients-model-multithreading-python/

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('Please enter your host address:\n')
port = int(input('Please enter a port (5477):\n'))

try:
    client.connect((host, port))
except socket.error as e:
    print(str(e))

while True:
    fromUser = input()
    client.sendall(str.encode(fromUser))
    fromServer = client.recv(1024)
    print(fromServer.decode())

client.close()

