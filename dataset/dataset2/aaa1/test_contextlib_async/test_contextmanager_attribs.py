import asyncio
from contextlib import asynccontextmanager, AbstractAsyncContextManager, AsyncExitStack, nullcontext, aclosing
import functools
from test import support
import unittest
from test.test_contextlib import TestBaseExitStack
import test_contextlib_async

def test_contextmanager_attribs():
    baz = AsyncContextManagerTestCase._create_contextmanager_attribs()
    AsyncContextManagerTestCase.assertEqual(baz.__name__, 'baz')
    AsyncContextManagerTestCase.assertEqual(baz.foo, 'bar')

AsyncContextManagerTestCase = test_contextlib_async.AsyncContextManagerTestCase()
test_contextmanager_attribs()
