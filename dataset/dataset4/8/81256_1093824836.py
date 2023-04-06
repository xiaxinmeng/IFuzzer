import asyncio
from unittest.mock import AsyncMock, call

async def main():
    a = AsyncMock()
    await a(1)
    a.assert_has_awaits([call(2)])

asyncio.run(main())