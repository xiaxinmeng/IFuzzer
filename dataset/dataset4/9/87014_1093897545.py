import asyncio

class Bar:
    def __init__(self):
        self.y = None

class Foo:
    def __init__(self):
        self._bar = Bar()
        self.y

    def __getattribute__(self, name):
        try:
            attr = super().__getattribute__(name)
        except AttributeError as e:
            try:
                attr = self.ooops_spelled_bar_wrong.__getattribute__(name)
            except AttributeError:
                raise e
        return attr

async def foo():
    Foo()

loop = asyncio.get_event_loop()
loop.create_task(foo())
loop.run_forever()