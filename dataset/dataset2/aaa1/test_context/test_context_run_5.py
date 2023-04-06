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

def test_context_run_5():
    ctx = contextvars.Context()
    var = contextvars.ContextVar('var')

    def func():
        ContextTest.assertIsNone(var.get(None))
        var.set('spam')
        1 / 0
    with ContextTest.assertRaises(ZeroDivisionError):
        ctx.run(func)
    ContextTest.assertIsNone(var.get(None))

ContextTest = test_context.ContextTest()
test_context_run_5()
