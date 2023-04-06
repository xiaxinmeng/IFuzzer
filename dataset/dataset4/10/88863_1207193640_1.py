
import asyncio
import argparse
import tracemalloc


class B:
    def __init__(self):
        self.some_big_data = bytearray(1024 * 1024)  # 1Mb for memory bloating

    async def doStuff(self):
        if not await self.connect():
            return
        print('Stuff done')

    async def connect(self) -> bool:
        try:
            _, writer = await asyncio.open_connection('127.0.0.1', 12345)
            writer.close()
            return True
        except OSError as e:
            pass
        return False


class A:
    def __init__(self, loop_count):
        self.loop_count = loop_count
        pass

    async def doBStuff(self):
        b = B()
        await b.doStuff()

    async def work(self):
        print('Working...')
        for _ in range(self.loop_count):
            await self.doBStuff()
        print('Done.')
        # print(
        #     'Memory usage {}mb'.format(
        #         int(resource.getrusage(
        #             resource.RUSAGE_SELF).ru_maxrss)//1000))
        current, peak = tracemalloc.get_traced_memory()
        print(f'cur = {current}, peak = {peak} from tracemalloc.get_traced_memory()')
        print("-"*30)


async def amain(loop_count):
    a = A(loop_count)
    await a.work()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--loop_count', type=int, nargs='?', default=10)
    args = parser.parse_args()

    tracemalloc.start()
    asyncio.run(amain(args.loop_count))

