import concurrent.futures
import contextvars
import functools
import gc
import random
import time
import unittest
import weakref
from _testcapi import hamt
import test_context

@test_context.isolated_context
def test_context_getset_5():
    c = contextvars.ContextVar('c', default=42)
    c.set([])

    def fun():
        c.set([])
        c.get().append(42)
        ContextTest.assertEqual(c.get(), [42])
    contextvars.copy_context().run(fun)
    ContextTest.assertEqual(c.get(), [])

ContextTest = test_context.ContextTest()
test_context_getset_5()
