import asyncio

def bug():
    loop.call_exception_handler({'message': 'bug!'})

def schedule_bug():
    bug()

loop = asyncio.get_event_loop()
loop.call_soon(schedule_bug)
loop.call_later(1, loop.stop)
loop.run_forever()
loop.close()