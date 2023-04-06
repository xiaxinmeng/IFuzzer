import asyncio
async def main():
    await asyncio.open_connection('localhost', 9990, local_addr=('localhost', 9991))
asyncio.run(main())