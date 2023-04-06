async def main(_loop):
    while True:
        with futures.ThreadPoolExecutor() as pool:
            _loop.run_in_executor(pool, nop)
        sys.stdout.write(f'\r{get_mem():0.3f}MB')