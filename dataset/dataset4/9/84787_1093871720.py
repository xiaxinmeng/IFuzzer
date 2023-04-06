import asyncio


async def ignore_cancel_and_raise():
    try:
        await asyncio.sleep(20)
    except asyncio.CancelledError:
        raise Exception('Cancellation failed')


async def main():
    try:
        await asyncio.wait_for(ignore_cancel_and_raise(), timeout=1)
    except asyncio.TimeoutError:
        print('Timeout')

asyncio.run(main())