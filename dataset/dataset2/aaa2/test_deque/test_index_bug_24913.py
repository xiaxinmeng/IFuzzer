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

def test_index_bug_24913():
    d = deque('A' * 3)
    with TestBasic.assertRaises(ValueError):
        i = d.index('Hello world', 0, 4)

TestBasic = test_deque.TestBasic()
test_index_bug_24913()
