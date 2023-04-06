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

def test_extend():
    d = deque('a')
    TestBasic.assertRaises(TypeError, d.extend, 1)
    d.extend('bcd')
    TestBasic.assertEqual(list(d), list('abcd'))
    d.extend(d)
    TestBasic.assertEqual(list(d), list('abcdabcd'))

TestBasic = test_deque.TestBasic()
test_extend()
