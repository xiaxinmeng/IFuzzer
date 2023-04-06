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

def test_contains_count_stop_crashes():

    class A:

        def __eq__(TestBasic, other):
            d.clear()
            return NotImplemented
    d = deque([A(), A()])
    with TestBasic.assertRaises(RuntimeError):
        _ = 3 in d
    d = deque([A(), A()])
    with TestBasic.assertRaises(RuntimeError):
        _ = d.count(3)

TestBasic = test_deque.TestBasic()
test_contains_count_stop_crashes()
