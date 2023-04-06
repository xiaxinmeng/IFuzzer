#!/usr/bin/env python
import SocketServer
usock = '/var/tmp/pong'

class PongHandler(SocketServer.DatagramRequestHandler):
    '''Play ping pong over datagram sockets
    '''
    def handle(self):
        '''Respond to any request with "Pong"
        '''
        pass
    def finish(self):
        '''Necessary under Linux to prevent:
           Exception:
           File "/usr/lib/python2.5/SocketServer.py", line 588, in finish
           self.socket.sendto(self.wfile.getvalue(), self.client_address)
           TypeError: argument must be string or read-only character
buffer, not
        '''
        if self.wfile.getvalue():
            SocketServer.DatagramRequestHandler.finish(self)

if __name__ == '__main__':
    SocketServer.UnixDatagramServer(usock, PongHandler).serve_forever()