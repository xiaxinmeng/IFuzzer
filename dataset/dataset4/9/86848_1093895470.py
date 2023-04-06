import asyncio

async def crash(key):
  raise Exception('crash!')

async def wait(fu):
  await fu

async def main():
  crasher = asyncio.create_task(crash(()))
  fs = [wait(crasher) for _ in range(10)]
  for fu in asyncio.as_completed(fs):
    try:
      await fu
    except Exception:
      import traceback
      traceback.print_exc()

if __name__ == '__main__':
  asyncio.run(main())