import asyncio, os
loop = asyncio.get_event_loop()
pid = os.fork()
if pid:
    print("parent", loop._csock.fileno(), loop._ssock.fileno())
else:
    print("child", loop._csock.fileno(), loop._ssock.fileno())