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

def test_repr():
    d = deque(range(200))
    e = eval(repr(d))
    TestBasic.assertEqual(list(d), list(e))
    d.append(d)
    TestBasic.assertEqual(repr(d)[-20:], '7, 198, 199, [...]])')

TestBasic = test_deque.TestBasic()
test_repr()
