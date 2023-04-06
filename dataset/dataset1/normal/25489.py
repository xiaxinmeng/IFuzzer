import sys
import asyncio

def handler(loop, context):
    print('Got error, exiting')
    sys.exit(42)

async def boom():
    await asyncio.sleep(0.1)
    raise Exception('boom')

loop = asyncio.get_event_loop()

# Schedule a call to hello_world()
loop.set_exception_handler(handler)
loop.create_task(boom())
#loop.run_forever()
