import sys
import select
import socket
import config

server = socket.socket()
clients = []
sock = socket.socket()
server.bind((config.ip, 8000))
server.listen(12)
conn, addr = server.accept()
data = conn.recv(99)

while True:
    if not data:
        print("Нет информации от пользователя")
        conn.close()
    else:
        print(data)
        clients.append(addr)
        print(clients)
        break


