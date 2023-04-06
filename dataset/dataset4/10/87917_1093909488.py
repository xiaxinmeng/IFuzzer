import asyncio

async def f():
    yield 'A'
    yield 'B'

async def main():
    g = f()
    print(await anext(g, 'Z'))  # Prints 'None' instead of 'A'!!!
    print(await anext(g, 'Z'))  # Prints 'None' instead of 'B'!!!
    print(await anext(g, 'Z'))  # Prints 'Z'
    g = f()
    print(await anext(g))       # Prints 'A'
    print(await anext(g))       # Prints 'B'
    print(await anext(g))       # Raises StopAsyncIteration

asyncio.run(main())