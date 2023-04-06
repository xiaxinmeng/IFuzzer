import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_increasingfrequency():
    for i in range(100, 2000, 100):
        safe_Beep(i, 75)

BeepTest = test_winsound.BeepTest()
test_increasingfrequency()
