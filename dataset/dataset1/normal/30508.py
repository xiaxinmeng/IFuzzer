import asyncio
loop = asyncio.get_event_loop()

async def crash():
    a = 1/0

async def main():
    t = asyncio.ensure_future(crash())
    await asyncio.sleep(1)
    t.cancel()

if __name__ == '__main__':
    loop.run_until_complete(main())
