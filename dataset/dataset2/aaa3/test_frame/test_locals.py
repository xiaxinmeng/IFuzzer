import re
import types
import unittest
import weakref
from test import support
import test_frame

def test_locals():
    (f, outer, inner) = FrameAttrsTest.make_frames()
    outer_locals = outer.f_locals
    FrameAttrsTest.assertIsInstance(outer_locals.pop('inner'), types.FunctionType)
    FrameAttrsTest.assertEqual(outer_locals, {'x': 5, 'y': 6})
    inner_locals = inner.f_locals
    FrameAttrsTest.assertEqual(inner_locals, {'x': 5, 'z': 7})

FrameAttrsTest = test_frame.FrameAttrsTest()
test_locals()
