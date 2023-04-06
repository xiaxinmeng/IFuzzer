import asyncio

class Foo:
    async def throw_exception(self):
        raise Exception("This is the inner exception")

    async def do_the_thing(self):
        try:
            await self.throw_exception()
        except Exception as e:
            raise Exception("This is the outer exception") from e

async def run():
    tasks = []

    foo = Foo()

    tasks.append(asyncio.create_task(foo.do_the_thing()))
    tasks.append(asyncio.create_task(foo.do_the_thing()))
    tasks.append(asyncio.create_task(foo.do_the_thing()))

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, Exception):
            print(f"Unexpected exception: {result}")

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())

if __name__ == "__main__":
    main()