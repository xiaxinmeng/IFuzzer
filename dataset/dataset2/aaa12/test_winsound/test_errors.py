import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_errors():
    BeepTest.assertRaises(TypeError, winsound.PlaySound)
    BeepTest.assertRaises(TypeError, winsound.PlaySound, 'bad', 'bad')
    BeepTest.assertRaises(RuntimeError, winsound.PlaySound, 'none', winsound.SND_ASYNC | winsound.SND_MEMORY)
    BeepTest.assertRaises(TypeError, winsound.PlaySound, b'bad', 0)
    BeepTest.assertRaises(TypeError, winsound.PlaySound, 'bad', winsound.SND_MEMORY)
    BeepTest.assertRaises(TypeError, winsound.PlaySound, 1, 0)
    BeepTest.assertRaises(ValueError, winsound.PlaySound, 'bad\x00', 0)

BeepTest = test_winsound.BeepTest()
test_errors()
