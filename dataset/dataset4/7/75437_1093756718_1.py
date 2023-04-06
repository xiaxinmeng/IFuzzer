# Wasteful: creates a new Lock object on every usage,
# regardless of whether it's actually needed.
async with lock_dict.setdefault(key, asyncio.Lock()):
    ...