async def f(n):
   await asyncio.sleep(n)
   return n

for f in asyncio.as_completed([f(3), f(2), f(1)]):
    print(await f)