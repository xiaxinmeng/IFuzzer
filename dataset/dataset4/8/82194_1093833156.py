import asyncio


class TestAsyncGenerator:
    def __init__(self):
        pass

    async def aiter(self):
        yield 1
        yield 2


async def main():
    gen = TestAsyncGenerator()
    async for number in gen.aiter():
        break


asyncio.run(main())