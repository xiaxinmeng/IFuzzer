import asyncio
from threading import Thread

def my_func():
    asyncio.new_event_loop()

t = Thread(target=my_func)
t.start()
t.join()