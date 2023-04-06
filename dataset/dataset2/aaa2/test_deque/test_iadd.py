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

def test_iadd():
    d = deque('a')
    d += 'bcd'
    TestBasic.assertEqual(list(d), list('abcd'))
    d += d
    TestBasic.assertEqual(list(d), list('abcdabcd'))

TestBasic = test_deque.TestBasic()
test_iadd()
