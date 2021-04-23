import sys
import select
import socket
import config


n = 1
server = socket.socket()
clients = {}
sock = socket.socket()
server.bind((config.ip, 8000))
server.listen(12)
conn, addr = server.accept()
data = conn.recv(99)

while True:
    if not data:
        print("Нет информации от пользователя")

    if data is data:
        if addr not in clients:
            clients[f'Игрок:{print(f"{addr}")}'] = addr
            print(clients)
            break



