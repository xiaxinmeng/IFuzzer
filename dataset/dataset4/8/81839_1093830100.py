
async def create_something():
    # this acquires some resource that needs explicit cleanup after some work
    return object()

def cleanup_something(inst):
    inst.close()

t = asyncio.ensure_future(create_something())
x = await asyncio.wait_for(t, timeout=10, cancel_handler=cleanup_something)
try:
    pass  # normal work with x
finally:
    cleanup_something(x)  # cleanup at normal execution