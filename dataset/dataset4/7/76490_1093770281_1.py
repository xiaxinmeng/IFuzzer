async def main():
    async with asyncio.ThreadPool(timeout=600) as pool:
        fut1 = pool.run(func)
        fut2 = pool.run(func, arg1, arg2)
        fut2 = pool.run(func, arg1, kwarg1=True)
    print(await asyncio.gather(fut1, fut2, fut3))

asyncio.run(main())