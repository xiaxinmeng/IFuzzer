import asyncio
from contextlib import asynccontextmanager, AbstractAsyncContextManager, AsyncExitStack, nullcontext, aclosing
import functools
from test import support
import unittest
from test.test_contextlib import TestBaseExitStack
import test_contextlib_async

@support.requires_docstrings
def test_instance_docs():
    cm_docstring = aclosing.__doc__
    obj = aclosing(None)
    AclosingTestCase.assertEqual(obj.__doc__, cm_docstring)

AclosingTestCase = test_contextlib_async.AclosingTestCase()
test_instance_docs()
