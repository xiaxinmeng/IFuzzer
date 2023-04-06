import asyncio
import sys

class MyProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        print('connection established')
        
    def data_received(self, data):
        print('received: {!r}'.format(data.decode()))
        
    def connection_lost(self, exc):
        print('lost connection')

if sys.platform.startswith('win32'):
    loop = asyncio.ProactorEventLoop()
else:
    loop = asyncio.SelectorEventLoop()
coro = loop.connect_read_pipe(MyProtocol, sys.stdin)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()