
import ssl
import certifi
import gc
import asyncio


ca_path = certifi.where()
async def make_async_context() -> None:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_verify_locations(ca_path)
    await asyncio.sleep(1)


async def main(n: int) -> None:
    await asyncio.wait([make_async_context() for _ in range(n)])


gc.collect()
asyncio.run(main(2000))
input("Finished run, still using lots of memory :(")
gc.collect()
input("gc.collect() does not help :(")
