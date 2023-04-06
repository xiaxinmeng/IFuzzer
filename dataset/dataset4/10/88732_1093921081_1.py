
import asyncio
import contextlib

@contextlib.asynccontextmanager
async def foo():
    yield

class StartIrritation(StopIteration):
    pass


async def amain():
    try:
        async with foo():
            raise StartIrritation
    except StartIrritation:
        print("good")
    except RuntimeError:
        print("bad")

asyncio.run(amain())
