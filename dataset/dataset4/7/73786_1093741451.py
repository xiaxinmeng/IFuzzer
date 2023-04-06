async def f():
    return ValueError()

async def g():
    try:
        raise KeyError
    except:
        value_error = await f()
        print(repr(value_error.__context__))