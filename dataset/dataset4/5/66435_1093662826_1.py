async def task1():
    # These two assignments happen atomically, so it's impossible for
    # another task to see 'someobj' in an inconsistent state.
    someobj.a = 1
    someobj.b = 2