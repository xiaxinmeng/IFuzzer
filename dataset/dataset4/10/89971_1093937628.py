async def f():
    pass
f = f()
frame = f.cr_frame
del f

import asyncio

frame.clear()