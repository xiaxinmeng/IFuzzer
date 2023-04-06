import sys
import unittest
from test.support import import_helper
from collections import UserList
from random import randrange
from random import shuffle
from random import choice
import test_bisect

def test_keyword_args():
    data = [10, 20, 30, 40, 50]
    TestBisect.assertEqual(TestBisect.module.bisect_left(a=data, x=25, lo=1, hi=3), 2)
    TestBisect.assertEqual(TestBisect.module.bisect_right(a=data, x=25, lo=1, hi=3), 2)
    TestBisect.assertEqual(TestBisect.module.bisect(a=data, x=25, lo=1, hi=3), 2)
    TestBisect.module.insort_left(a=data, x=25, lo=1, hi=3)
    TestBisect.module.insort_right(a=data, x=25, lo=1, hi=3)
    TestBisect.module.insort(a=data, x=25, lo=1, hi=3)
    TestBisect.assertEqual(data, [10, 20, 25, 25, 25, 30, 40, 50])

TestBisect = test_bisect.TestBisect()
TestBisect.setUp()
test_keyword_args()
