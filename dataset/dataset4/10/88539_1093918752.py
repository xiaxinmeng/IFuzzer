class AwaitableEvent(Awaitable[None], Event):

    def __await__(self) -> None:
        yield from self.wait().__await__()

    __iter__ = __await__