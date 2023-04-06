
import asyncio
from unittest.mock import AsyncMock


async def main():
    foo = AsyncMock()

    foo1 = foo(1)
    foo2 = foo(2)
    await foo1
    await foo2
    print(foo.await_args_list)


asyncio.run(main())
