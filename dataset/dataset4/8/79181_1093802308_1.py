class Test(object):

    async def other(self):
        print('Hello!')

    async def __aenter__(self):
        pass

    async def __aexit__(self, a, b, c):
        await asyncio.shield(self.other())

async def func():
    async with Test():
        await asyncio.sleep(5)

def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(func())
    except KeyboardInterrupt:
        pass
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()

if __name__ == '__main__':
    main()