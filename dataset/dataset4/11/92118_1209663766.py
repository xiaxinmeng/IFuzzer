import contextlib


@contextlib.asynccontextmanager
async def f():
    try:
        yield
    finally:
        pass

async def amain():
    async with f(): 1/0


with contextlib.closing(amain().__await__()) as gen:
    next(gen, None)