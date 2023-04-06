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

def test_context_new_1():
    with ContextTest.assertRaisesRegex(TypeError, 'any arguments'):
        contextvars.Context(1)
    with ContextTest.assertRaisesRegex(TypeError, 'any arguments'):
        contextvars.Context(1, a=1)
    with ContextTest.assertRaisesRegex(TypeError, 'any arguments'):
        contextvars.Context(a=1)
    contextvars.Context(**{})

ContextTest = test_context.ContextTest()
test_context_new_1()
