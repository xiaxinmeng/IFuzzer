import asyncio
import contextvars
import threading

var = contextvars.ContextVar('var')
var.set('spam')


def doit():
    print(f"thread: {var.get()}")


async def async_sub_doit():
    print(f"async sub: {var.get()}")


async def async_doit():
    print(f"async: {var.get()}")
    var.set('span2')
    print(f"async: {var.get()}")
    await asyncio.create_task(async_sub_doit())

print(f"main: {var.get()}")

try:
    thread = threading.Thread(target=doit)
    thread.start()
    thread.join()
except Exception as e:
    print(f"Thread exception: {e}")

asyncio.run(async_doit())