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
def test_context_getset_4():
    c = contextvars.ContextVar('c', default=42)
    ctx = contextvars.Context()
    tok = ctx.run(c.set, 1)
    with ContextTest.assertRaisesRegex(ValueError, 'different Context'):
        c.reset(tok)

ContextTest = test_context.ContextTest()
test_context_getset_4()
