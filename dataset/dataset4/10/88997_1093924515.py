import asyncio
import contextvars


ctxvar = contextvars.ContextVar("ctxvar", default="spam")


def func():
    assert ctxvar.get() == "spam"

async def coro():
    func()


async def main():
    ctx = contextvars.copy_context()
    ctxvar.set("ham")
    ctx.run(func)  # works
    await ctx.run(coro)  # breaks

asyncio.run(main())