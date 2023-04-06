import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_weakref():
    weakref.ref(AddressTestCase_v4.factory('2001:db8::'))
    weakref.ref(AddressTestCase_v4.factory('2001:db8::%scope'))

AddressTestCase_v4 = test_ipaddress.AddressTestCase_v4()
test_weakref()
