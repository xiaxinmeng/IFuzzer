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

def test_context_typerrors_1():
    ctx = contextvars.Context()
    with ContextTest.assertRaisesRegex(TypeError, 'ContextVar key was expected'):
        ctx[1]
    with ContextTest.assertRaisesRegex(TypeError, 'ContextVar key was expected'):
        1 in ctx
    with ContextTest.assertRaisesRegex(TypeError, 'ContextVar key was expected'):
        ctx.get(1)

ContextTest = test_context.ContextTest()
test_context_typerrors_1()
