#!/usr/bin/env python3

import socket
HOST = "127.0.0.1" #The server's hostname or IP address
PORT = 65432  #The port used by server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, User')
    data = s.recv(1024)

print("Received",repr(data))
