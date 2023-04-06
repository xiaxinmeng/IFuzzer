import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_bad_address_split_v6_not_enough_parts():

    def assertBadSplit(addr):
        msg = 'At least 3 parts expected in %r'
        with AddressTestCase_v6.assertAddressError(msg, addr.split('%')[0]):
            ipaddress.IPv6Address(addr)
    assertBadSplit(':')
    assertBadSplit(':1')
    assertBadSplit('FEDC:9878')
    assertBadSplit(':%scope')
    assertBadSplit(':1%scope')
    assertBadSplit('FEDC:9878%scope')

AddressTestCase_v6 = test_ipaddress.AddressTestCase_v6()
test_bad_address_split_v6_not_enough_parts()
