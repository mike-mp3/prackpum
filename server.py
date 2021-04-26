import socket
import config

n = 1
server = socket.socket()
clients = {0: 'Server'}
sock = socket.socket()
server.bind((config.ip, 8000))
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
            clients[f"{n}"] = f'{addr}'
            print(str(addr) + ' присоединился.')
        else:
            conn.close()


    print(clients)
