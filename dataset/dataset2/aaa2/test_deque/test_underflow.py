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

def test_underflow():
    d = deque()
    TestBasic.assertRaises(IndexError, d.pop)
    TestBasic.assertRaises(IndexError, d.popleft)

TestBasic = test_deque.TestBasic()
test_underflow()
