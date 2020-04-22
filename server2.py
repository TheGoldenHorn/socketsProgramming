#!/usr/bin/env python3
import socket

HOST = "127.0.0.1"  #Standard loopback interface address aka localhost
PORT = 65432        #Port to listen on (non-privileged ports are >1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #use socket object without calling socket.close()
    #.socket() specifies address family
    #AF_INET is IPv4 address
    #.SOCK_STREAM is for TCP protocol; It will be used to transport our messages
    
    s.bind((HOST,PORT)) #Associate the socket with specified network interface and port    #Depends on address family of the socket. IPv4 expects a tuple containing IP and Port


    s.listen(2) #enable the server to accept() connections
    #backlog parameter will specify number of unaccepted connections allowed before refusing new connections


    conn, addr = s.accept() #blocks and waits for an incoming connection. s.accept() returns new socket object representing the connecting and a tuple containing the client address.
    
    with conn:
        print("Connected By: ",addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
