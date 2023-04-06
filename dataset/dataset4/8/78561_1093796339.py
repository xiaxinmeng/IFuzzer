async def force_async(obj):
    """Force an object to be asynchronous"""
    if hasattr(obj, '__await__'):
        return await obj
    async def inner():
        return obj
    return await inner()