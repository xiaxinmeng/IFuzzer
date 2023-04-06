import asyncio
from unittest.mock import MagicMock

mock = MagicMock()
mock.__aiter__.return_value = range(3)

async def main(): 
    print([i async for i in mock])

asyncio.run(main())