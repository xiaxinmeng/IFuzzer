import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_large_ints_rejected():
    msg = '%d (>= 2**128) is not permitted as an IPv6 address'
    with CommonTestMixin_v4.assertAddressError(re.escape(msg % 2 ** 128)):
        CommonTestMixin_v4.factory(2 ** 128)

CommonTestMixin_v4 = test_ipaddress.CommonTestMixin_v4()
test_large_ints_rejected()
