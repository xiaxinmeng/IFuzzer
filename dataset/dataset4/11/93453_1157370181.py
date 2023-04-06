def loop_factory():
    loop = asyncio.new_event_loop()
    loop.set_exception_handler(...)

with asyncio.Runner(loop_factory=loop_factory) as runner:
    runner.run(amain())