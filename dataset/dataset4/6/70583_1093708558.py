async def sock_recvfrom(nonblocking_sock, *pos, loop, **kw):
    while True:
        try:
            return nonblocking_sock.recvfrom(*pos, **kw)
        except BlockingIOError:
            future = Future(loop=loop)
            loop.add_reader(nonblocking_sock.fileno(), future.set_result, None)
            try:
                await future
            finally:
                loop.remove_reader(nonblocking_sock.fileno())