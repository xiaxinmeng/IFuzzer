
class TimedTask(asyncio.Task):

    self.cputime = 0.0

    def _step(self, *args, **kwargs):
        start = time.time()
        super()._step(*args, **kwargs)
        self.cputime += time.time() - start

