lock = lock_dict.get(key)
if lock is None:
    lock = lock_dict[key] = asyncio.Lock()
async with lock:
    ...