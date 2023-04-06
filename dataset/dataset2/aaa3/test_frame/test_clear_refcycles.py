import re
import types
import unittest
import weakref
from test import support
import test_frame

@support.cpython_only
def test_clear_refcycles():
    with support.disable_gc():

        class C:
            pass
        c = C()
        wr = weakref.ref(c)
        exc = ClearTest.outer(c=c)
        del c
        ClearTest.assertIsNot(None, wr())
        ClearTest.clear_traceback_frames(exc.__traceback__)
        ClearTest.assertIs(None, wr())

ClearTest = test_frame.ClearTest()
test_clear_refcycles()
