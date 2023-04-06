from collections import deque
import unittest
from test import support, seq_tests
import gc
import weakref
import copy
import pickle
import random
import struct
import gc
import sys
import gc
from test import test_deque
import test_deque

def test_extendleft():
    d = deque('a')
    TestBasic.assertRaises(TypeError, d.extendleft, 1)
    d.extendleft('bcd')
    TestBasic.assertEqual(list(d), list(reversed('abcd')))
    d.extendleft(d)
    TestBasic.assertEqual(list(d), list('abcddcba'))
    d = deque()
    d.extendleft(range(1000))
    TestBasic.assertEqual(list(d), list(reversed(range(1000))))
    TestBasic.assertRaises(SyntaxError, d.extendleft, test_deque.fail())

TestBasic = test_deque.TestBasic()
test_extendleft()
