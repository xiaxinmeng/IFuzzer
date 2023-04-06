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

def test_context_run_3():
    ctx = contextvars.Context()

    def func(*args, **kwargs):
        1 / 0
    with ContextTest.assertRaises(ZeroDivisionError):
        ctx.run(func)
    with ContextTest.assertRaises(ZeroDivisionError):
        ctx.run(func, 1, 2)
    with ContextTest.assertRaises(ZeroDivisionError):
        ctx.run(func, 1, 2, a=123)

ContextTest = test_context.ContextTest()
test_context_run_3()
