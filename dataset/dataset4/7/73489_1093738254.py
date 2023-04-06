import asyncio

lock = asyncio.Lock()

def a ():
 yield from lock.acquire()
 for i in range(10):
  print('b: ' + str(i))
  if i % 2 == 0:
   lock.release()
   yield from lock.acquire()
 lock.release()

async def b ():
 print('hello')