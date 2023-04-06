import unittest
from test import support
from test.support import warnings_helper
import gc
import weakref
import operator
import copy
import pickle
from random import randrange, shuffle
import warnings
import collections
import collections.abc
import itertools
from itertools import chain
import test_set

def test_uniquification():
    actual = sorted(TestJointOps.s)
    expected = sorted(TestJointOps.d)
    TestJointOps.assertEqual(actual, expected)
    TestJointOps.assertRaises(PassThru, TestJointOps.thetype, check_pass_thru())
    TestJointOps.assertRaises(TypeError, TestJointOps.thetype, [[]])

TestJointOps = test_set.TestJointOps()
test_uniquification()
