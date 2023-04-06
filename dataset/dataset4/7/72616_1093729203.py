fut = asyncio.Future()  # C implemented version of asyncio.Future
it = iter(fut)  # Iterator of it
it.send(42)     # raised TypeError before. It was not compatible with Python version of asyncio.Future