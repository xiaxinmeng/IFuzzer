import asyncio
from contextvars import ContextVar
import contextvars

ctx = ContextVar("test")

ctx.set("global")
print('expected to be "global":', ctx.get())


async def main():
    ctx.set("inner")
    print('expected to be "inner":', ctx.get())
    try:
        await asyncio.sleep(5) # may exit here
        raise Exception("this is the expected case")
    except BaseException as e:
        print('in except, expected to be "inner":', ctx.get())
        raise e
    finally:
        print('in finally, expected to be "inner":', ctx.get())

asyncio.run(main())