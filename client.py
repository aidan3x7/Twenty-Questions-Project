# Client File
# Aidan Liljehorn
# CS 330
# Credit/Sources: Bek Brace & ProgrammingKnowledge on YouTube (Guiding the code that is presented here).


import socket

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 10821))
    client.send(b'hello')
    message = client.recv(1024)

    printOut = client.send()
    printIn = client.recv()





