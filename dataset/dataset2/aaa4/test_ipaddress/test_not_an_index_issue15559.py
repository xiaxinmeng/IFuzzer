import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_not_an_index_issue15559():
    CommonTestMixin.assertRaises(TypeError, operator.index, CommonTestMixin.factory(1))
    CommonTestMixin.assertRaises(TypeError, hex, CommonTestMixin.factory(1))
    CommonTestMixin.assertRaises(TypeError, bytes, CommonTestMixin.factory(1))

CommonTestMixin = test_ipaddress.CommonTestMixin()
test_not_an_index_issue15559()
