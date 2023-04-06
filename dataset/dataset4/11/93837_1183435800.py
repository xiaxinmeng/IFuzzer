
import asyncio
import functools
import sys

sys.setrecursionlimit(3000)

def test():
  fut = asyncio.Future()
  def done_cb(arg):
    pass
  fut.add_done_callback(functools.partial(done_cb, fut))

  print(repr(fut))

try:
  test()
except:
  print("Done")
