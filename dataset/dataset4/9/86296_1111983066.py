from . import timeouts

async def wait_for(aw, timeout):
    async with timeouts.timeout(timeout):
        return await aw