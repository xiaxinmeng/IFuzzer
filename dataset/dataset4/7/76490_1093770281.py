class ThreadPool:
    def __init__(self, timeout=None):
        self.timeout = timeout
        self._loop = None
    
    async def __aenter__(self):
        self._loop = asyncio.get_running_loop()
        # Ensure that ThreadPoolExecutor is being used
        self._loop.default_executor = concurrent.futures.ThreadPoolExecutor()
        return self

    async def __aexit__(self, *args):
        await self._loop.shutdown_default_executor(timeout=self.timeout)

    def run(self, func, *args, **kwargs):
        call = functools.partial(func, *args, **kwargs)
        return self._loop.run_in_executor(None, call)