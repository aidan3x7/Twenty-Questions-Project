# Client File
# Aidan Liljehorn
# CS 330
# Credit/Sources: Bek Brace & ProgrammingKnowledge on YouTube (Guiding the code that is presented here).


import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 10821))

while True:
    sending = str(input('Type something\n'))
    bytes_sending = str.encode(sending)
    client.sendall(bytes_sending)
    message = client.recv(1024)

    #printOut = client.send()
    #printIn = client.recv()

    print('Received', repr(message))





