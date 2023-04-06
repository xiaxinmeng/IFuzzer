import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_default():
    MessageBeepTest.assertRaises(TypeError, winsound.MessageBeep, 'bad')
    MessageBeepTest.assertRaises(TypeError, winsound.MessageBeep, 42, 42)
    safe_MessageBeep()

MessageBeepTest = test_winsound.MessageBeepTest()
test_default()
