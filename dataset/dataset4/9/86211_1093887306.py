import asyncio

async def f() -> int:
    return 1

async def main():
    breakpoint()

asyncio.run(main())