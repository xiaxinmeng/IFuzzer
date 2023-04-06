loop = asyncio.new_event_loop()
loop.run_until_complete(func())
loop.run_until_complete(loop.shutdown_asyncgens())
loop.close()