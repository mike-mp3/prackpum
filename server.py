import socket
import config
import sys
import select

n = 1
server = socket.socket()
clients = []
sock = socket.socket()
server.bind((config.ip, 8001))
server.listen(3)
conn, addr = server.accept()

while True:
    data = conn.recv(99)
    print("Поиск...")
    if not data:
        print("Нет информации от пользователя")
        conn.close()

    if addr not in clients:
        if n < 5:
            for n in clients:
                n += 1
            clients.append(conn)
            print(str(addr) + ' присоединился.')
        else:
            conn.close()
    sockets = [sys.stdin, server] + clients
    ins = select.select([], [], 0)
    for sock in ins:
        if sock is select.stdin:
            sys.stdin()
        elif sock is sock:
            sock.close()


    print(clients)
