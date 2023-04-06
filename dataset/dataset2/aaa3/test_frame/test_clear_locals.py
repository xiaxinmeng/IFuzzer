import re
import types
import unittest
import weakref
from test import support
import test_frame

def test_clear_locals():
    (f, outer, inner) = ClearTest.make_frames()
    outer.clear()
    inner.clear()
    ClearTest.assertEqual(outer.f_locals, {})
    ClearTest.assertEqual(inner.f_locals, {})

ClearTest = test_frame.ClearTest()
ClearTest.setUp()
test_clear_locals()
