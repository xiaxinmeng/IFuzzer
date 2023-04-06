async def setup(self):
    self.server = await self.loop.create_server(...)

async def teardown(self):
    await self.server.wait_closed()