async def coroutine():
    return 123
coro = coroutine()

# In Python 3.5.1:
print(await coro)   # will print 123
print(await coro)   # prints None
print(await coro)   # prints None

# What we want in Python 3.5.2
print(await coro)   # will print 123
print(await coro)   # raises RuntimeError