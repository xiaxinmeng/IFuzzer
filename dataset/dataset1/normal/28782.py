import asyncio

loop = asyncio.get_event_loop()


class Connection:
    def read_until(self, *args, **kwargs):
        return self

    async def all(self):
        return b"\n"


class Cursor:
    def __init__(self):
        self._connection = Connection()
        self._max_bytes = 100
        self._data = bytearray()

    async def _read_data(self):
        # XXX segfault there, if I change anything in the code, it works...
        while True:
            data = await self._connection.read_until(
                b'\n', max_bytes=self._max_bytes).all()
            self._max_bytes -= len(data)
            if data == b'\n':
                break
            self._data.extend(data)


async def main():
    await Cursor()._read_data()


loop.run_until_complete(main())
