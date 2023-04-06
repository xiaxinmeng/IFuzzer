def not_coro():
    yield


async def main():
    await gather(not_coro()) # will not fail
    await not_coro() # will fail