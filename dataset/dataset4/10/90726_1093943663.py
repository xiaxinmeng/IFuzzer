class TestConnections(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.proxy = asyncio.create_task(EnergyAgentProxy(self.proxy_port, self.server_port, self.upstream_port))

    async def asyncTearDown(self) -> None:
        await asyncio.sleep(1)