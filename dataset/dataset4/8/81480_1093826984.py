from asyncio import run


async def true():
    return True


async def false():
    return False


async def error():
    a = false()
    b = true()
    return await (a or b)
    # Good Error
    #   "RuntimeWarning: coroutine 'true' was never awaited print(await error())"


async def no_error():
    return await (false() or true())  # False
    # Bad Problem
    #   `RuntimeWarning` is not raised for 'true'.