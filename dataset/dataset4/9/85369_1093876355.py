class SomeAPI:
    ...

    async def request(self):
        pass

    async def close(self):
        await self.session.close()
        

async with closing(SomeAPI()) as api:
    response = await api.request()
    print(response)