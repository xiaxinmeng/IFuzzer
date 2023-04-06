import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_pickle():
    AddressTestCase_v4.pickle_test('2001:db8::1000/124')
    AddressTestCase_v4.pickle_test('2001:db8::1000/127')
    AddressTestCase_v4.pickle_test('2001:db8::1000')
    AddressTestCase_v4.pickle_test('2001:db8::1000%scope')

AddressTestCase_v4 = test_ipaddress.AddressTestCase_v4()
test_pickle()
