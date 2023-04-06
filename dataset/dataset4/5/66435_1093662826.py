async def f():
    print("hi from f()")
    await g()

async def g():
    print("hi from g()")

# This is our event loop:
coro = f()
try:
    coro.send(None)
except StopIteration:
    pass