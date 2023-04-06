import asyncio

async def count_smth(seconds: int) -> int:
    await asyncio.sleep(seconds)
    return seconds * 3

async def small_job(d: dict, key: str, seconds: int) -> None:
    d[key] += await count_smth(seconds)  # <-- strange happens here

async def main() -> None:
     d = dict(key=0)
     await asyncio.gather(
           small_job(d, 'key', 1),
           small_job(d, 'key', 2),
     )
     print(d['key'])  # expected: 0 + 1 * 3 + 2 * 3 = 9, actual: 6

if __name__ == '__main__':
    asyncio.run(main())