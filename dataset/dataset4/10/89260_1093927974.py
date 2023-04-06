import asyncio
import warnings

warnings.filterwarnings('error')

def crash():
    raise KeyboardInterrupt

async def main():
    asyncio.get_event_loop().call_soon(crash)
    await asyncio.sleep(5)