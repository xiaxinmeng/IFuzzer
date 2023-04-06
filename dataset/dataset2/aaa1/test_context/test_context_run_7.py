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

def test_context_run_7():
    ctx = contextvars.Context()

    def fun():
        with ContextTest.assertRaisesRegex(RuntimeError, 'is already entered'):
            ctx.run(fun)
    ctx.run(fun)

ContextTest = test_context.ContextTest()
test_context_run_7()
