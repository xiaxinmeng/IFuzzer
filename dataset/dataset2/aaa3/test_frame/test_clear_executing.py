import re
import types
import unittest
import weakref
from test import support
import test_frame

def test_clear_executing():
    try:
        1 / 0
    except ZeroDivisionError as e:
        f = e.__traceback__.tb_frame
    with ClearTest.assertRaises(RuntimeError):
        f.clear()
    with ClearTest.assertRaises(RuntimeError):
        f.f_back.clear()

ClearTest = test_frame.ClearTest()
test_clear_executing()
