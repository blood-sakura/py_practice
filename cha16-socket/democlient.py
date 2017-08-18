#!/usr/bin/env python

from socket import *

_host='localhost'
_port=21567
_bufsiz=1024
_addr=(_host, _port)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(_addr)
    data = raw_input('>')

    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(_bufsiz)

    if not data:
        break

    print data.strip()
    tcpCliSock.close()
