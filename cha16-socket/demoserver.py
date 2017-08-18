#!/usr/bin/env python

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

_host=''
_port=21567
_addr=(_host,_port)

class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

tcpServ = TCP(_addr, MyRequestHandler)
print 'waiting for connection...'

tcpServ.serve_forever()