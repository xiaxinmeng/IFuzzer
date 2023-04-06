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

def test_init():
    TestBasic.assertRaises(TypeError, deque, 'abc', 2, 3)
    TestBasic.assertRaises(TypeError, deque, 1)

TestBasic = test_deque.TestBasic()
test_init()
