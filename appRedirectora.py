#!/usr/bin/python

"""
Seila Oliva Muñoz

Con navegador Chrome ha llegado a más de 20.000 redirecciones y con navegador
Firefox ha llegado a más de 2.000 redirecciones, y no se ha detenido en ningun
caso, lo que lleva a pensar que puede hacer infinitas redirecciones a urls
aleatorias
"""

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

while True:
    a = random.randint(0, 1000000000)
    dir = "http://localhost:1234/" + str(a)

    print ('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print ('HTTP request received:')
    print (recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 302 Redirect\r\n\r\n" +
                          "<html><body><h1>Redireccionando a:<br></h1>" + dir +
                          "<meta http-equiv='Refresh' content='0;url=dir" +
                          "'></body></html>" +
                          "\r\n", "utf-8"))
    recvSocket.close()
