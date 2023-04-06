async def read(self, *args):
    try:
        self._fileobj.read(*args, nonblock=True)
    except BlockingIOError: # maybe?
        return await run_in_worker_thread(self._fileobj.read, *args)