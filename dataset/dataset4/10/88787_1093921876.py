import linecache, sys

def trace(frame, event, arg):
    # The weird globals here is to avoid a NameError on shutdown...
    if frame.f_code.co_filename == globals().get("__file__"):
        lineno = frame.f_lineno
        print("{} {}: {}".format(event[:4], lineno, linecache.getline(__file__, lineno).rstrip()))
    return trace

import asyncio

async def async_gen():
    yield 13

async def async_test():
    global a
    a = 17
    async for i in async_gen():
        print(i + 19)
    else:
        a = 21

print(sys.version)
sys.settrace(trace)

asyncio.run(async_test())
assert a == 21