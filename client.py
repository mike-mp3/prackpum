import socket
import config

sock = socket.socket()
sock.connect((config.ip, 8001))
sock.send(b'done')
data = sock.recv(99)


