# Server File
# Aidan Liljehorn
# CS 330
# Credit/Sources: Bek Brace & ProgrammingKnowledge on YouTube (Guiding the code that is presented here).

import threading
import twenty_questions_protocol
import socket

host = "127.0.0.1"
port = 10821

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []

def broadcast(message):
    for client in clients:
        client.send(message)

def connection():
    print("[SERVER]: Running & Listening")
    client, address = server.accept()
    print("[SERVER]: Connection ", address, " accepted.")
    clients.append(client)
    client.send("[CLIENT]: You're now connected.".encode("utf-8"))

def server_register():
    client = clients[0]
    twenty_questions_protocol.register(client)

def server_login():
    client = clients[0]
    twenty_questions_protocol.login(client, username, password)

connection()

def runnable():
    twenty_questions_protocol.register(client)
    twenty_questions_protocol.login(client,username,password)
    twenty_questions_protocol.twenty_qs()


runnable()


