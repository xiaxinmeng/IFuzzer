import types
import traceback

async def a():
    return await b()

async def b():
    return await c()

@types.coroutine
def c():
    try:
        traceback.print_stack()
        yield len(traceback.extract_stack())
    except ZeroDivisionError:
        traceback.print_stack()
        yield len(traceback.extract_stack())
        
r = a()
print(r.send(None))
print(r.throw(ZeroDivisionError))
