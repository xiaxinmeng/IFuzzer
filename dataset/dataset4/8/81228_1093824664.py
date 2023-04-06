import asyncio
from unittest.mock import create_autospec

async def foo(): pass

spec = create_autospec(foo)
awaitable = spec()

async def main(): await awaitable

asyncio.run(main())