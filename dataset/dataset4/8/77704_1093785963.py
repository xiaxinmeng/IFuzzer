def sync_call(arg):
    asyncio.get_event_loop().run_until_complete(async_call(arg))