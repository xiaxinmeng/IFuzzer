import asyncio
from contextlib import asynccontextmanager, AbstractAsyncContextManager, AsyncExitStack, nullcontext, aclosing
import functools
from test import support
import unittest
from test.test_contextlib import TestBaseExitStack
import test_contextlib_async

@support.requires_docstrings
def test_contextmanager_doc_attrib():
    baz = AsyncContextManagerTestCase._create_contextmanager_attribs()
    AsyncContextManagerTestCase.assertEqual(baz.__doc__, 'Whee!')

AsyncContextManagerTestCase = test_contextlib_async.AsyncContextManagerTestCase()
test_contextmanager_doc_attrib()
