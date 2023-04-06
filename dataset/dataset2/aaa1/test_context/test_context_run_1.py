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

def test_context_run_1():
    ctx = contextvars.Context()
    with ContextTest.assertRaisesRegex(TypeError, 'missing 1 required'):
        ctx.run()

ContextTest = test_context.ContextTest()
test_context_run_1()
