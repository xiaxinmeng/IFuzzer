import socket
import asyncio

loop = asyncio.get_event_loop()


sock = socket.socket()
sock.close()

async def client():
	reader, writer = await asyncio.open_connection(
	    sock=sock,
	    loop=loop)

async def runner():
	await client()

loop.run_until_complete(runner())
