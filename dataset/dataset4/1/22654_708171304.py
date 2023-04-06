import asyncio
import unittest

class TestHangsForever(unittest.IsolatedAsyncioTestCase):
    async def test_hangs_forever(self):
        task = asyncio.create_task(asyncio.sleep(1))
        task.cancel()
        await task

if __name__ == "__main__":
    import unittest
    unittest.main()