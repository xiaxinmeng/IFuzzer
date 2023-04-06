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

def test_context_run_6():
    ctx = contextvars.Context()
    c = contextvars.ContextVar('a', default=0)

    def fun():
        ContextTest.assertEqual(c.get(), 0)
        ContextTest.assertIsNone(ctx.get(c))
        c.set(42)
        ContextTest.assertEqual(c.get(), 42)
        ContextTest.assertEqual(ctx.get(c), 42)
    ctx.run(fun)

ContextTest = test_context.ContextTest()
test_context_run_6()
