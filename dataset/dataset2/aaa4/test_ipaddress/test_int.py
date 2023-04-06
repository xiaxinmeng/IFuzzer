import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_int():
    CommonTestMixin_v4.assertInstancesEqual(0, '::')
    CommonTestMixin_v4.assertInstancesEqual(3232235521, '::c0a8:1')

CommonTestMixin_v4 = test_ipaddress.CommonTestMixin_v4()
test_int()
