import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_extremes():
    safe_Beep(37, 75)
    safe_Beep(32767, 75)

BeepTest = test_winsound.BeepTest()
test_extremes()
