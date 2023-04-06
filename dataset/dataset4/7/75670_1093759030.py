executor = ProcessPoolExecutor(...)
executor.submit(lambda: None).wait()
with asyncio.get_event_loop() as loop:
    loop.run_until_complete(...)