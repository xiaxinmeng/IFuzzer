import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_bad_address_split_v6_too_many_parts_with_double_colon():

    def assertBadSplit(addr):
        msg = "Expected at most 7 other parts with '::' in %r"
        with AddressTestCase_v6.assertAddressError(msg, addr.split('%')[0]):
            ipaddress.IPv6Address(addr)
    assertBadSplit('1:2:3:4::5:6:7:8')
    assertBadSplit('1:2:3:4::5:6:7:8%scope')

AddressTestCase_v6 = test_ipaddress.AddressTestCase_v6()
test_bad_address_split_v6_too_many_parts_with_double_colon()
