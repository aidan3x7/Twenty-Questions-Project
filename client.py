# Client File
# Aidan Liljehorn
# CS 330
# Credit/Sources: Bek Brace & ProgrammingKnowledge on YouTube (Guiding the code that is presented here).


import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 10821))

while True:
    fromUser = input()
    fromUser = str.encode(fromUser)
    client.sendall(fromUser)
    fromServer = client.recv(1024)
    fromServer = fromServer.decode()
    print(fromServer)





