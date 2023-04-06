
import asyncio

async def action(loop):
    proc = await asyncio.create_subprocess_exec('echo', loop=loop)
    await proc.wait()

loop = asyncio.new_event_loop()
loop.run_until_complete(action(loop))
loop.close()
