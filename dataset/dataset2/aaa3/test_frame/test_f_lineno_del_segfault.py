import re
import types
import unittest
import weakref
from test import support
import test_frame

def test_f_lineno_del_segfault():
    (f, _, _) = FrameAttrsTest.make_frames()
    with FrameAttrsTest.assertRaises(AttributeError):
        del f.f_lineno

FrameAttrsTest = test_frame.FrameAttrsTest()
test_f_lineno_del_segfault()
