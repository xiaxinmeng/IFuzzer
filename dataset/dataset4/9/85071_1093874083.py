
# childfut.py
import asyncio

async def f(fut):
    await fut

async def g(t):
    await asyncio.sleep(t)

async def main():
    fut_g = asyncio.create_task(g(1))
    fut_f = asyncio.create_task(f(fut_g))

    try:

        # Cancel the "child" future
        fut_g.cancel()

        await fut_f
    except asyncio.CancelledError as e:
        pass

    print(f'fut_f done? {fut_f.done()} fut_f cancelled? {fut_f.cancelled()}')
    print(f'fut_g done? {fut_g.done()} fut_g cancelled? {fut_g.cancelled()}')

asyncio.run(main())
