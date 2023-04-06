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

def test_reversed():
    for s in ('abcd', range(2000)):
        TestBasic.assertEqual(list(reversed(deque(s))), list(reversed(s)))

TestBasic = test_deque.TestBasic()
test_reversed()
