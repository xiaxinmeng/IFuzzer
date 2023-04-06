import asyncio
from threading import Thread

# Work-around from https://bugs.python.org/issue34679
policy = asyncio.get_event_loop_policy()
policy._loop_factory = asyncio.SelectorEventLoop

def my_func():
    asyncio.new_event_loop()

t = Thread(target=my_func)
t.start()
t.join()