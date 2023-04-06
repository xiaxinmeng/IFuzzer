
@asynccontextmanager
async def ctx():
    yield


async def gen():
    async with ctx():
        yield 'hello'
        yield 'world'


async def main():
    async with ctx():
        async for value in gen():
            print(value)
            raise RuntimeError()
