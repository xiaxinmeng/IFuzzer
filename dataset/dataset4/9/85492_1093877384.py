workaround = False

async def slow_proc():
  proc = await asyncio.create_subprocess_exec('sleep', '10', stdout=asyncio.subprocess.PIPE)
  try:
    return await proc.stdout.read()
  except asyncio.CancelledError:
    if workaround:
      proc.terminate()
      time.sleep(0.1)  # hope the machine is not too busy

async def func():
  try:
    return await asyncio.wait_for(slow_proc(), timeout=0.1)
  except asyncio.TimeoutError:
    return 'timeout'

def main():
  while True:
    print('test')
    asyncio.run(func())

main()