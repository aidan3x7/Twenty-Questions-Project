# Client File
# Aidan Liljehorn
# CS 330
# Credit/Sources: Bek Brace & ProgrammingKnowledge on YouTube (Guiding the code that is presented here).


import socket
username = input("Enter a username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 10821))

def client_connection():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "username?":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("[ERROR]")
            client.close()
