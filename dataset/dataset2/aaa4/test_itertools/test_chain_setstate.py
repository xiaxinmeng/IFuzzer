import unittest
from test import support
from itertools import *
import weakref
from decimal import Decimal
from fractions import Fraction
import operator
import random
import copy
import pickle
from functools import reduce
import sys
import struct
import threading
import gc
import gc
import test_itertools

def test_chain_setstate():
    TestBasicOps.assertRaises(TypeError, chain().__setstate__, ())
    TestBasicOps.assertRaises(TypeError, chain().__setstate__, [])
    TestBasicOps.assertRaises(TypeError, chain().__setstate__, 0)
    TestBasicOps.assertRaises(TypeError, chain().__setstate__, ([],))
    TestBasicOps.assertRaises(TypeError, chain().__setstate__, (iter([]), []))
    it = chain()
    it.__setstate__((iter(['abc', 'def']),))
    TestBasicOps.assertEqual(list(it), ['a', 'b', 'c', 'd', 'e', 'f'])
    it = chain()
    it.__setstate__((iter(['abc', 'def']), iter(['ghi'])))
    TestBasicOps.assertEqual(list(it), ['ghi', 'a', 'b', 'c', 'd', 'e', 'f'])

TestBasicOps = test_itertools.TestBasicOps()
test_chain_setstate()
