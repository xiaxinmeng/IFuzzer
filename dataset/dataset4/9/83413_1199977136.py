import asyncio
from asyncio.subprocess import create_subprocess_exec
from unittest import IsolatedAsyncioTestCase
import subprocess

class Test83413(IsolatedAsyncioTestCase):

    async def asyncSetUp(self) -> None:
        self.p = await create_subprocess_exec('notepad', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # This will cause an error because we're not cleaning up the open pipes

    async def test_simple(self):
        await asyncio.sleep(1)
        assert True is False