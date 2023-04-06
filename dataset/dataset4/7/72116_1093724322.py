import asyncio
import socket
sock = socket.socket(family=socket.AF_BLUETOOTH,
                     type=socket.SOCK_STREAM,
                     proto=socket.BTPROTO_RFCOMM)
sock.setblocking(False)
addr = "00:12:34:56:78:99"
loop = asyncio.get_event_loop()
loop.run_until_complete(loop.sock_connect(sock, (addr, 1)))