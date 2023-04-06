import asyncio
import unittest


class DemonstrateHang(unittest.IsolatedAsyncioTestCase):
    async def test_hang(self):
        task = asyncio.create_task(asyncio.sleep(2))
        await asyncio.sleep(0.1)
        task.cancel()
        await task
        # this also hangs: await asyncio.wait_for(task, 5)