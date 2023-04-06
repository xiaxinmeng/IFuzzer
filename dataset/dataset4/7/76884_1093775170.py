async def open_file():
    pass

async def main():
    async with open_file():  # Should be 'async with await open_file()'
        pass

coro = main()
coro.send(None)