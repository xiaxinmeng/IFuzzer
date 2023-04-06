import sys
import unittest
from test.support import import_helper
from collections import UserList
from random import randrange
from random import shuffle
from random import choice
import test_bisect

def test_backcompatibility():
    TestBisect.assertEqual(TestBisect.module.insort, TestBisect.module.insort_right)

TestBisect = test_bisect.TestBisect()
TestBisect.setUp()
test_backcompatibility()
