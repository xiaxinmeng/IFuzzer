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

def test_context_subclassing_1():
    with ContextTest.assertRaisesRegex(TypeError, 'not an acceptable base type'):

        class MyContextVar(contextvars.ContextVar):
            pass
    with ContextTest.assertRaisesRegex(TypeError, 'not an acceptable base type'):

        class MyContext(contextvars.Context):
            pass
    with ContextTest.assertRaisesRegex(TypeError, 'not an acceptable base type'):

        class MyToken(contextvars.Token):
            pass

ContextTest = test_context.ContextTest()
test_context_subclassing_1()
