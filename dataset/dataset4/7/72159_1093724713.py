import asyncio


class A:
    @asyncio.coroutine
    def start(self):
        self.runner_task = asyncio.ensure_future(self.runner())

    @asyncio.coroutine
    def stop(self):
        self.runner_task.cancel()
        yield from self.runner_task

    @asyncio.coroutine
    def runner(self):
        try:
            while True:
                yield from asyncio.sleep(5)
        except asyncio.CancelledError:
            yield from self.stop()
            return


def do_test():
    @asyncio.coroutine
    def f():
        a = A()
        yield from a.start()
        yield from asyncio.sleep(1)
        yield from a.stop()