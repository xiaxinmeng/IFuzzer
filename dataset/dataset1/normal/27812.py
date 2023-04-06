# execute this with "python -Werror"
import gc
async def f():
    pass
cr = f()
frame = cr.cr_frame
del cr
gc.collect()
# create some randomness to reuse the memory just freed by 'cr'
import asyncio
print("ping")
frame.clear()
