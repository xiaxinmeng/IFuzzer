# -- good code --
async def agen_fn():
    yield

async def do_good_thing():
    agen = agen_fn()
    await agen.aclose()
    # Should *not* raise an error, but currently does in Python dev branches:
    await agen.aclose()

asyncio.run(do_good_thing())