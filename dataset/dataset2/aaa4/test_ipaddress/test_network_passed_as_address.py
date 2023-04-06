import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_network_passed_as_address():

    def assertBadSplit(addr):
        msg = "Unexpected '/' in %r"
        with AddressTestCase_v4.assertAddressError(msg, addr):
            ipaddress.IPv6Address(addr)
    assertBadSplit('::1/24')
    assertBadSplit('::1%scope_id/24')

AddressTestCase_v4 = test_ipaddress.AddressTestCase_v4()
test_network_passed_as_address()
