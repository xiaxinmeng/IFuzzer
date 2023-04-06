def call_async(func, *args):
    return asyncio.get_event_loop().run_in_executor(func, *arg)