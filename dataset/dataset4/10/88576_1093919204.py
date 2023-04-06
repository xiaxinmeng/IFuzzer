
import sys
import unittest
from unittest.mock import AsyncMock


class A:
    async def foobar(self):
        while True:
            try:
                return await self.mock()
            except Exception:
                continue


class TestA(unittest.IsolatedAsyncioTestCase):
    async def test_refcount(self):
        a = A()
        a.mock = AsyncMock(side_effect=[Exception(), None])
        refc = sys.getrefcount(a)
        await a.foobar()
        self.assertEqual(refc, sys.getrefcount(a))


if __name__ == "__main__":
    unittest.main()
