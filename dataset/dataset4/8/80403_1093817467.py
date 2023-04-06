
import asyncio
from unittest.mock import Mock


class AsyncMock(Mock):

    def __call__(self, *args, **kwargs):
        sup = super(AsyncMock, self)
        async def coro():
            return sup.__call__(*args, **kwargs)
        return coro()

    def __await__(self):
        return self().__await__()

mocked_function = AsyncMock()

asyncio.run(asyncio.gather(mocked_function()))
