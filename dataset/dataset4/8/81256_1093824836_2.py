import asyncio
from unittest.mock import AsyncMock, call

async def main():
    a = AsyncMock()
    await a(1)
    a(2)
    a.assert_awaited_with(2)

asyncio.run(main())