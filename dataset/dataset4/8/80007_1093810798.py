cond = asyncio.Condition()

# ... later
await lock.acquire()
try:
    await cond.wait()
finally:
    lock.release()