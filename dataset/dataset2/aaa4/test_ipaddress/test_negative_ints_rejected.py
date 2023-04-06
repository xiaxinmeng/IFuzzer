import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_negative_ints_rejected():
    msg = '-1 (< 0) is not permitted as an IPv6 address'
    with CommonTestMixin_v4.assertAddressError(re.escape(msg)):
        CommonTestMixin_v4.factory(-1)

CommonTestMixin_v4 = test_ipaddress.CommonTestMixin_v4()
test_negative_ints_rejected()
