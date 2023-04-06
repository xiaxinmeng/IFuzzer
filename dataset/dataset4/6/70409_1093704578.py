import asyncio

class AsyncIteratorWrapper:

    def __init__(self, iterable, loop=None, executor=None):
        self._iterator = iter(iterable)
        self._loop = loop or asyncio.get_event_loop()
        self._executor = executor

    async def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return await self._loop.run_in_executor(
                    self._executor, next, self._iterator)
        except StopIteration:
            raise StopAsyncIteration