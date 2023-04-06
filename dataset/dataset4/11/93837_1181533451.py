import sys
sys.setrecursionlimit(3000)
import asyncio
import functools

def test():
  fut = asyncio.Future()
  def done_cb(arg):
    pass
  fut.add_done_callback(functools.partial(done_cb, fut))

  print(repr(fut))

test()