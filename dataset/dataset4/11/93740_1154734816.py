from contextvars import ContextVar
import asyncio
from signal import raise_signal
from contextlib import ExitStack

test = ContextVar("test")
loop = asyncio.new_event_loop()

test.set("global")
print('expected to be "global":', test.get())


async def main():
    test.set("inner")
    with ExitStack() as stack:
        stack.push(lambda *args: print('expected to be "inner":', test.get()))
        print('expected to be "inner":', test.get())
        await asyncio.sleep(5)


loop.run_until_complete(main())