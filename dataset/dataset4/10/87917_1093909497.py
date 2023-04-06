import asyncio

class CustomAsyncIter:
    def __init__(self):
        self.iterator = iter(['A', 'B'])
    def __aiter__(self):
        return self
    async def __anext__(self):
        try:
            x = next(self.iterator)
        except StopIteration:
            raise StopAsyncIteration from None
        await asyncio.sleep(1)
        return x

async def main1():
    iter1 = CustomAsyncIter()
    print(await anext(iter1))       # Prints 'A'
    print(await anext(iter1))       # Prints 'B'
    print(await anext(iter1))       # Raises StopAsyncIteration

async def main2():
    iter1 = CustomAsyncIter()
    print('Before')                 # Prints 'Before'
    print(await anext(iter1, 'Z'))  # Silently terminates the script!!!
    print('After')                  # This never gets executed

asyncio.run(main2())