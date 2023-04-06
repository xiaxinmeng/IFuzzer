
import asyncio

loop = asyncio.get_event_loop()

def func():
    pass

f = loop.run_in_executor(None, func)
loop.stop()
loop.run_forever()
loop.stop()
loop.run_forever()
loop.stop()
loop.run_forever()
