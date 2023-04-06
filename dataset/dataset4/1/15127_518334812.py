import asyncio
import unittest

from unittest.async_case import IsolatedAsyncioTestCase

class FooTest(IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        print("Async Setup")

    async def test_sleep(self):
        await asyncio.sleep(1)
        self.assertEqual(1, 1)

    async def asyncTearDown(self):
        print("Async Teardown")

if __name__ == "__main__":
    unittest.main()