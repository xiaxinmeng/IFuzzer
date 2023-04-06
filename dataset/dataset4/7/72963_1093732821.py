import asyncio, sanic

class MyQueue(asyncio.Queue):
    def __aiter__(self): return self
    async def __anext__(self): return await self.get()

app = sanic.Sanic()
ws_set = set()
app.static('/', 'async.html')