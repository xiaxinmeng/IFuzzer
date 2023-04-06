_unset = ['unset']
class CachedAwaitable:
    def __init__(self, awaitable):
        self.awaitable = awaitable
        self.result = _unset
    def __await__(self):
        if self.result is _unset:
            self.result = yield from self.awaitable.__await__()
        return self.result