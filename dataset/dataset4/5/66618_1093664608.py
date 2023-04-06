import asyncio
@asyncio.coroutine
def main():
    raise KeyboardInterrupt
asyncio.get_event_loop().run_until_complete(main())