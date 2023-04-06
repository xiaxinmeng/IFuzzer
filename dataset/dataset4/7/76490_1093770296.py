class ThreadPool:
    def __init__(self, timeout=None):
        self.timeout = timeout
        self._loop = asyncio.get_event_loop()
        self._executor = concurrent.futures.ThreadPoolExecutor()

    async def close(self): 
        await self._executor.shutdown(timeout=self.timeout)  
        
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()

    def run(self, func, *args, **kwargs):
        call = functools.partial(func, *args, **kwargs)
        return self._loop.run_in_executor(self._executor, call)