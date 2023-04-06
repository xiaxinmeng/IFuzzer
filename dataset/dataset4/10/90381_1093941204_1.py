
class TestSyncJobs(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        init_test_env()

        await emit.start(engine=emit.Engine.REDIS, dsn=cfg.redis.dsn, start_server=True, heart_beat=1)

        await self.create_quotes_fetcher()

        # if we add the following line, the issue will gone
        # await asyncio.sleep(0.01)
        await omicron.init(aq)
