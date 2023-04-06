import asyncio
loop = asyncio.ProactorEventLoop()
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.open_connection("::1", 4242))