import asyncio
loop = asyncio.get_event_loop()

asyncio.iscoroutinefunction(loop.sock_recv)
False

asyncio.iscoroutine(loop.sock_recv)
False