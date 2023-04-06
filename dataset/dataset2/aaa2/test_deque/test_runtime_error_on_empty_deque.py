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

def test_runtime_error_on_empty_deque():
    d = deque()
    it = iter(d)
    d.append(10)
    TestVariousIteratorArgs.assertRaises(RuntimeError, next, it)

TestVariousIteratorArgs = test_deque.TestVariousIteratorArgs()
test_runtime_error_on_empty_deque()
