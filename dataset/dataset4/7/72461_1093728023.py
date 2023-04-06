import asyncio
async def run():
    raise RuntimeError
def exception_handler(loop, context):
    print('Made it to exception handler.')
loop = asyncio.get_event_loop()
loop.set_exception_handler(exception_handler)
loop.create_task(run())
loop.run_forever()