# -- bad code --
async def agen_fn():
    yield

async def do_bad_thing():
    agen = agen_fn()
    aclose_coro = agen.aclose()
    await aclose_coro
    # Should raise RuntimeError:
    await aclose_coro

asyncio.run(do_bad_thing())