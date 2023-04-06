
async def f1():
  return await f2()

async def f2():
  return await asyncio.ensure_future(f3())

async def f3():
  return await f4()

async def f4():
  await asyncio.sleep(10)
  return 42
