import resource
import asyncio


class B:
    def __init__(self, loop):
        self.loop = loop
        self.some_big_data = bytearray(1024 * 1024)  # 1Mb for memory bloating

    async def doStuff(self):
        if not await self.connect():
            return
        print('Stuff done')

    async def connect(self) -> bool:
        try:
            _, writer = await asyncio.open_connection('127.0.0.1', 12345, loop=self.loop)
            writer.close()
            return True
        except OSError as e:
            pass
        return False


class A:
    def __init__(self, loop):
        self.loop = loop

    async def doBStuff(self):
        b = B(self.loop)
        await b.doStuff()

    async def work(self):
        print('Working...')
        for _ in range(1000):
            await self.loop.create_task(self.doBStuff())
        print('Done.')
        print(
            'Memory usage {}kb'.format(
                resource.getrusage(
                    resource.RUSAGE_SELF).ru_maxrss))


async def amain(loop):
    a = A(loop)
    await a.work()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(amain(loop))