import asyncio


async def process(idx: int, semaphore: asyncio.Semaphore) -> None:
    while True:
        async with semaphore:
            print(f'ACQUIRE {idx}')
            await asyncio.sleep(1)


async def main() -> None:
    semaphore = asyncio.Semaphore(5)
    await asyncio.gather(*[process(idx, semaphore) for idx in range(20)])

asyncio.run(main())