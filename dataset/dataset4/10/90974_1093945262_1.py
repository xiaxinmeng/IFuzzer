class ContextOpener(
    Coroutine[Any, Any, Feed],
    AbstractAsyncContextManager[Feed],
):
    __slots__ = ("_wrapped_coro", "_feed_cls", "_feed")

    def __init__(self, opener_coro: Coroutine, feed_cls: Type[Feed]):
        self._wrapped_coro = opener_coro
        self._feed_cls = feed_cls