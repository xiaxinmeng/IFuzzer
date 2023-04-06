with asyncio.Runner() as runner:
    runner.get_loop().set_exception_handler(...)
    runner.run(amain())