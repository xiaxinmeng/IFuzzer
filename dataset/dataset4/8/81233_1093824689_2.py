import asyncio
from unittest.mock import MagicMock

class WithAsyncContextManager:

    async def __aenter__(self, *args, **kwargs):
        return self

    async def __aexit__(self, *args, **kwargs):
        pass

instance = WithAsyncContextManager()
mock_instance = MagicMock(instance)

async def main():
    async with mock_instance as result:
        print("entered")

asyncio.run(main())