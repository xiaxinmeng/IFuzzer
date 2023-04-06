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

def test_context_var_new_1():
    with ContextTest.assertRaisesRegex(TypeError, 'takes exactly 1'):
        contextvars.ContextVar()
    with ContextTest.assertRaisesRegex(TypeError, 'must be a str'):
        contextvars.ContextVar(1)
    c = contextvars.ContextVar('aaa')
    ContextTest.assertEqual(c.name, 'aaa')
    with ContextTest.assertRaises(AttributeError):
        c.name = 'bbb'
    ContextTest.assertNotEqual(hash(c), hash('aaa'))

ContextTest = test_context.ContextTest()
test_context_var_new_1()
