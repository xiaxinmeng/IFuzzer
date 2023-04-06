import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_empty_octet():

    def assertBadOctet(addr):
        with AddressTestCase_v4.assertAddressError('Empty octet not permitted in %r', addr):
            ipaddress.IPv4Address(addr)
    assertBadOctet('42..42.42')
    assertBadOctet('...')

AddressTestCase_v4 = test_ipaddress.AddressTestCase_v4()
test_empty_octet()
