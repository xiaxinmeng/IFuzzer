import sys
import unittest
from test.support import import_helper
from collections import UserList
from random import randrange
from random import shuffle
from random import choice
import test_bisect

def test_negative_lo():
    mod = TestBisect.module
    TestBisect.assertRaises(ValueError, mod.bisect_left, [1, 2, 3], 5, -1, 3)
    TestBisect.assertRaises(ValueError, mod.bisect_right, [1, 2, 3], 5, -1, 3)
    TestBisect.assertRaises(ValueError, mod.insort_left, [1, 2, 3], 5, -1, 3)
    TestBisect.assertRaises(ValueError, mod.insort_right, [1, 2, 3], 5, -1, 3)

TestBisect = test_bisect.TestBisect()
test_negative_lo()
