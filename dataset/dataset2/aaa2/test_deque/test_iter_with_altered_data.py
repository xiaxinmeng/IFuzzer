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

def test_iter_with_altered_data():
    d = deque('abcdefg')
    it = iter(d)
    d.pop()
    TestVariousIteratorArgs.assertRaises(RuntimeError, next, it)

TestVariousIteratorArgs = test_deque.TestVariousIteratorArgs()
test_iter_with_altered_data()
