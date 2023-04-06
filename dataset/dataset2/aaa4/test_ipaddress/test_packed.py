import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_packed():
    addr = b'\x00' * 12 + bytes.fromhex('00000000')
    CommonTestMixin_v4.assertInstancesEqual(addr, '::')
    addr = b'\x00' * 12 + bytes.fromhex('c0a80001')
    CommonTestMixin_v4.assertInstancesEqual(addr, '::c0a8:1')
    addr = bytes.fromhex('c0a80001') + b'\x00' * 12
    CommonTestMixin_v4.assertInstancesEqual(addr, 'c0a8:1::')

CommonTestMixin_v4 = test_ipaddress.CommonTestMixin_v4()
test_packed()
