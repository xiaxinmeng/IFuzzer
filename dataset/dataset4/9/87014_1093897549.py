import asyncio

class Test(Exception):
    ...

def x():
    raise Test('Hello World!')

def bar():
    try:
        x()
    except Test as e:
        try:
            bar()
        except Test as e:
            raise e

async def foo():
    bar()

loop = asyncio.get_event_loop()
loop.create_task(foo())
loop.run_forever()