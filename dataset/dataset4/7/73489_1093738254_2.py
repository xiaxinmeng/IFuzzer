import asyncio

lock = asyncio.Lock()

def a ():
 yield from lock.acquire()
 yield from asyncio.sleep(0)
 for i in range(10):
  print('a: ' + str(i))
  if i % 2 == 0:
   lock.release()
   yield from lock.acquire()
 lock.release()

def b ():
 yield from lock.acquire()
 yield from asyncio.sleep(0)
 for i in range(10):
  print('b: ' + str(i))
  if i % 2 == 0:
   lock.release()
   yield from lock.acquire()
 lock.release()