
import asyncio
import ssl
import certifi


async def f():
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(cafile=certifi.where())
    await asyncio.open_connection('example.org', 443, ssl=ssl_context)


loop = asyncio.get_event_loop()
loop.run_until_complete(f())
loop.close()
