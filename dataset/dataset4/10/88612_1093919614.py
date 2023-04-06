import traceback
import io

async def foo():
    yield 1
    traceback.print_stack(file=io.StringIO())
    yield 2

async def bar():
    return [chunk async for chunk in foo()]