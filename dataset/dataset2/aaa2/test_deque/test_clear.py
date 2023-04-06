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

def test_clear():
    d = deque(range(100))
    TestBasic.assertEqual(len(d), 100)
    d.clear()
    TestBasic.assertEqual(len(d), 0)
    TestBasic.assertEqual(list(d), [])
    d.clear()
    TestBasic.assertEqual(list(d), [])

TestBasic = test_deque.TestBasic()
test_clear()
