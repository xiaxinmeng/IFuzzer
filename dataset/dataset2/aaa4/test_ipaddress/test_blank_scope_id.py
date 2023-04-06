import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_blank_scope_id():
    address = '::1%'
    with CommonTestMixin_v6.assertAddressError('Invalid IPv6 address: "%r"', address):
        CommonTestMixin_v6.factory(address)

CommonTestMixin_v6 = test_ipaddress.CommonTestMixin_v6()
test_blank_scope_id()
