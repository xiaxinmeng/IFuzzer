import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_leading_zeros():
    CommonTestMixin_v4.assertInstancesEqual('0000::0000', '::')
    CommonTestMixin_v4.assertInstancesEqual('000::c0a8:0001', '::c0a8:1')

CommonTestMixin_v4 = test_ipaddress.CommonTestMixin_v4()
test_leading_zeros()
