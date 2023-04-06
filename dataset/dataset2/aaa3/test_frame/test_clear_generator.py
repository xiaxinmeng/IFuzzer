import re
import types
import unittest
import weakref
from test import support
import test_frame

def test_clear_generator():
    endly = False

    def g():
        nonlocal endly
        try:
            yield
            ClearTest.inner()
        finally:
            endly = True
    gen = g()
    next(gen)
    ClearTest.assertFalse(endly)
    gen.gi_frame.clear()
    ClearTest.assertTrue(endly)

ClearTest = test_frame.ClearTest()
test_clear_generator()
