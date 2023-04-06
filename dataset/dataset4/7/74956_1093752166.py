
import asyncio


async def generator():
    while True:
        x = yield 42
        print("received", x)
        await asyncio.sleep(0.1)


async def user(name, g):
    print("sending", name)
    await g.asend(name)


async def helper():
    g = generator()
    await g.asend(None)

    await asyncio.gather(*(user(f"user-{x}", g) for x in range(3)))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(helper())
