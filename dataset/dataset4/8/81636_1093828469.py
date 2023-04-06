
import asyncio


async def count():
    try:
        i = 0
        while True:
            yield i
            i += 1
    finally:
        print("count() cleanup")


async def double(source):
    try:
        async for n in source:
            yield n * 2
    finally:
        print("double() cleanup")


async def main():
    async for i in double(count()):
        if i > 10:
            return
        print(i)

asyncio.run(main())
