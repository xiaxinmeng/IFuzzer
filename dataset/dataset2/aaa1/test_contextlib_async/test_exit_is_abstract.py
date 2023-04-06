import asyncio
from contextlib import asynccontextmanager, AbstractAsyncContextManager, AsyncExitStack, nullcontext, aclosing
import functools
from test import support
import unittest
from test.test_contextlib import TestBaseExitStack
import test_contextlib_async

def test_exit_is_abstract():

    class MissingAexit(AbstractAsyncContextManager):
        pass
    with TestAbstractAsyncContextManager.assertRaises(TypeError):
        MissingAexit()

TestAbstractAsyncContextManager = test_contextlib_async.TestAbstractAsyncContextManager()
test_exit_is_abstract()
