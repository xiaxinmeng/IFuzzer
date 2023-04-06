import asyncio
import sys
import unittest

import asyncio

asyncio.set_child_watcher(asyncio.PidfdChildWatcher())


def create_free_port():
    return 4  # chosen by a fair dice roll


class TestProc(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.port = create_free_port()
        self.proc = await asyncio.create_subprocess_exec(
            sys.executable,
            "-c",  # more realistically this might be an http server or database
            f"import time; print('listening on {self.port}'); import time; time.sleep(2); print('goodbye')",
        )

    async def testProc(self):
        print(f"connecting to {self.port}")

    async def asyncTearDown(self):
        await self.proc.communicate()  # hangs forever on 3.11


if __name__ == "__main__":
    unittest.main()