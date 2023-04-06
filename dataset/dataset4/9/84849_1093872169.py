import asyncio


async def return_42_on_cancel():
    try:
        await asyncio.sleep(20)
    except asyncio.CancelledError:
        return 42  # `return` is useless in this block.


async def main():
    try:
        await asyncio.wait_for(return_42_on_cancel(), timeout=1)
    except asyncio.TimeoutError:
        print('Timeout')

asyncio.run(main())