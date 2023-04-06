import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_aclose_compatible_with_get_stack():

    async def async_generator():
        yield object()

    async def run():
        ag = async_generator()
        test_asyncgen.asyncio.create_task(ag.aclose())
        tasks = test_asyncgen.asyncio.all_tasks()
        for task in tasks:
            task.get_stack()
    AsyncGenAsyncioTest.loop.run_until_complete(run())

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_aclose_compatible_with_get_stack()
