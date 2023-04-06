lock_dict = WeakValueDictionary(default=asyncio.Lock)

async with lock_dict[key]:
    ...