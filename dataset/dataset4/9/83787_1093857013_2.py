# -- good code --
async def agen_fn():
    yield

async def careful_loop():
    agen = agen_fn()
    try:
        async for _ in agen:
            pass
    finally:
        await agen.aclose()

asyncio.run(careful_loop())