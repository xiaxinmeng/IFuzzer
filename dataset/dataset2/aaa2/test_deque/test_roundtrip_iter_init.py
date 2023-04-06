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

def test_roundtrip_iter_init():
    d = deque(range(200))
    e = deque(d)
    TestBasic.assertNotEqual(id(d), id(e))
    TestBasic.assertEqual(list(d), list(e))

TestBasic = test_deque.TestBasic()
test_roundtrip_iter_init()
