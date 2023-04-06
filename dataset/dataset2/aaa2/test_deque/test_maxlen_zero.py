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

def test_maxlen_zero():
    it = iter(range(100))
    deque(it, maxlen=0)
    TestBasic.assertEqual(list(it), [])
    it = iter(range(100))
    d = deque(maxlen=0)
    d.extend(it)
    TestBasic.assertEqual(list(it), [])
    it = iter(range(100))
    d = deque(maxlen=0)
    d.extendleft(it)
    TestBasic.assertEqual(list(it), [])

TestBasic = test_deque.TestBasic()
test_maxlen_zero()
