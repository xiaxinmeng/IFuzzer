@types.coroutine
def _yield():
    yield

async def func():
    async with acm():
        # GeneratorExit raised here
        await _yield()

x = func()
x.send(None) # start running func
x.close() # raise GeneratorExit in func at its current yield
# AsyncContextManager __aexit__ fails with "RuntimeError: generator didn't stop after throw()"