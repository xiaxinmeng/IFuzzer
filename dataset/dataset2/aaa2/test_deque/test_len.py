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

def test_len():
    d = deque('ab')
    TestBasic.assertEqual(len(d), 2)
    d.popleft()
    TestBasic.assertEqual(len(d), 1)
    d.pop()
    TestBasic.assertEqual(len(d), 0)
    TestBasic.assertRaises(IndexError, d.pop)
    TestBasic.assertEqual(len(d), 0)
    d.append('c')
    TestBasic.assertEqual(len(d), 1)
    d.appendleft('d')
    TestBasic.assertEqual(len(d), 2)
    d.clear()
    TestBasic.assertEqual(len(d), 0)

TestBasic = test_deque.TestBasic()
test_len()
