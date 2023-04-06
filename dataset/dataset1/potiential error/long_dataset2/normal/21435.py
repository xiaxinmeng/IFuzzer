import asyncio
 
class A:
    pass
 
class B:
    def __init__(self, future):
        self.future = future
 
    def __del__(self):
        self.a = None
 
@asyncio.coroutine
def do_work(future):
    a = A()
    b = B(asyncio.Future())
 
    a.b = b
    b.a = a
 
    future.set_result(None)
 
future = asyncio.Future()
asyncio.Task(do_work(future))
loop = asyncio.get_event_loop()
loop.run_until_complete(future)
