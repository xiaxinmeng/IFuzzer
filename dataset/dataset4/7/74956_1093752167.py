
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

    u0 = asyncio.ensure_future(user("user-0", g))
    u1 = asyncio.ensure_future(user("user-1", g))
    u2 = asyncio.ensure_future(user("user-2", g))

    await u0
    await u1
    await u2


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(helper())
