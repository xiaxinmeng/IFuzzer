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

def test_context_get_context_1():
    ctx = contextvars.copy_context()
    ContextTest.assertIsInstance(ctx, contextvars.Context)

ContextTest = test_context.ContextTest()
test_context_get_context_1()
