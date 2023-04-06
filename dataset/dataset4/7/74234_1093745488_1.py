@a.coroutine
def coro1():
    yield from a.ensure_future(coro2())
    print("Still here")
    yield from a.sleep(.1)
    print("Still here 2")

@a.coroutine
def coro2():
    yield from a.sleep(.1)
    res = task.cancel()
    print("Canceled task:", res)
    yield from a.sleep(.1)  # !!! added this line

loop = a.get_event_loop()
task = a.ensure_future(coro1())
loop.run_until_complete(task)