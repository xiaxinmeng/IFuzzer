import asyncio
import unittest


class TestCancellation(unittest.IsolatedAsyncioTestCase):

    async def test_works(self):
        raise asyncio.CancelledError()


if __name__ == '__main__':
    unittest.main()