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

def test_maxlen_attribute():
    TestBasic.assertEqual(deque().maxlen, None)
    TestBasic.assertEqual(deque('abc').maxlen, None)
    TestBasic.assertEqual(deque('abc', maxlen=4).maxlen, 4)
    TestBasic.assertEqual(deque('abc', maxlen=2).maxlen, 2)
    TestBasic.assertEqual(deque('abc', maxlen=0).maxlen, 0)
    with TestBasic.assertRaises(AttributeError):
        d = deque('abc')
        d.maxlen = 10

TestBasic = test_deque.TestBasic()
test_maxlen_attribute()
