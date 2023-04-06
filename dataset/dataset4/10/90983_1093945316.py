import socket
import asyncio

async def amain():
    with socket.socket(family=socket.AF_INET, proto=socket.IPPROTO_UDP, type=socket.SOCK_DGRAM) as sock:
        sock.setblocking(False)
        await asyncio.get_running_loop().sock_connect(sock, ("google.com", "443"))

asyncio.run(amain())