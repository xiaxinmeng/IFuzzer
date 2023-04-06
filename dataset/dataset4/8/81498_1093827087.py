import asyncio


class CustomException(BaseException):  # It works if base class changed to Exception
    pass


async def do_this(x):
    if x == 5:
        raise CustomException()
    await asyncio.sleep(1)
    print(f'THIS DONE: {x}')


async def main():
    print('BEGIN')
    tasks = [do_this(x) for x in range(1, 11)]
    result = await asyncio.gather(*tasks, return_exceptions=True)
    print(f'Result: {result}')
    print('END')


asyncio.run(main())