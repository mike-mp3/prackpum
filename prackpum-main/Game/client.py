import socket

sock = socket.socket()
sock.connect(('10.171.132.115', 8000))
sock.send(b'work')
data = sock.recv(99)

