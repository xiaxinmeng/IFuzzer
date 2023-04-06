async def foo(a, b): pass

async def main():
    task = asyncio.create_task(foo(1, b=1))
    task1 = asyncio.create_task(foo(1, b=task))
    print(repr(task))
    print(repr(task1))

asyncio.run(main())