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
def test_context_getset_2():
    v1 = contextvars.ContextVar('v1')
    v2 = contextvars.ContextVar('v2')
    t1 = v1.set(42)
    with ContextTest.assertRaisesRegex(ValueError, 'by a different'):
        v2.reset(t1)

ContextTest = test_context.ContextTest()
test_context_getset_2()
