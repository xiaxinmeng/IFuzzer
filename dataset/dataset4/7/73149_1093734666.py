
import asyncio

fut = asyncio.Future()
fut.add_done_callback(str)

for _ in range(63):
    fut.add_done_callback(id)

class evil:
    def __eq__(self, other):
        fut.remove_done_callback(id)
        return False

fut.remove_done_callback(evil())
