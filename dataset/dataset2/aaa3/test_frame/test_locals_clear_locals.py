import re
import types
import unittest
import weakref
from test import support
import test_frame

def test_locals_clear_locals():
    (f, outer, inner) = FrameAttrsTest.make_frames()
    outer.f_locals
    inner.f_locals
    outer.clear()
    inner.clear()
    FrameAttrsTest.assertEqual(outer.f_locals, {})
    FrameAttrsTest.assertEqual(inner.f_locals, {})

FrameAttrsTest = test_frame.FrameAttrsTest()
test_locals_clear_locals()
