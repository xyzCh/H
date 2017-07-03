#!/usr/bin/python


import socket
import os
from implRouter import implRouter
import xmlParser

HOST, PORT = '', int(xmlParser.Parser()["port"])

def rp(client_connection):
    request = client_connection.recv(1024)
    header=request.decode()
    if len(header)==0:
        pass
    else:
        implRouter(header,client_connection).Exec()
        
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(5)

print ('Start HTTP Service on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    pid=os.fork()
    if pid==0:
        rp(client_connection)
        client_connection.close()
        os._exit(0)
    else:
        client_connection.close()
