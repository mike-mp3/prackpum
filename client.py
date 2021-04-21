import socket

sock = socket.socket()
sock.connect(('192.168.1.68', 8000))
sock.send(b'hello, world!')

data = sock.recv(99)
sock.close()
