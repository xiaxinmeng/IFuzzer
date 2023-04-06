class Foo:
    @functools.cache
    async def go(self):
        print(1)

async def main():
    foo = Foo()
    await foo.go()
    await foo.go()