# Server File
# Aidan Liljehorn
# CS 330
# Credit/Sources: Bek Brace & ProgrammingKnowledge on YouTube (Guiding the code that is presented here).

import threading
import socket
host = "127.0.0.1"
port = 10821

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def connection():
    print("[SERVER]: Running & Listening")
    client, address = server.accept()
    print("[SERVER]: Connection ", address, " accepted.")
    client.send("username?".encode("utf-8"))
    username = client.recv(1024)
    usernames.append(username)
    clients.append(client)
    print("[SERVER]: ", username.encode("utf-8"))
    broadcast("[SERVER]: ", username, " has logged in.".encode("utf-8"))
    client.send("[CLIENT]: You're now connected.".encode("utf-8"))


connection()
