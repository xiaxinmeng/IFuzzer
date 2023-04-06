from unittest.mock import AsyncMock


class Foo:

    def foo(self):
        pass

    async def bar(self):
        pass

m = AsyncMock(Foo)
f = m()
print(m.foo)
print(m.bar)