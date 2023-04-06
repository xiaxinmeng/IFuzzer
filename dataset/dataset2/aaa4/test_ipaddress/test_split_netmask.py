import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_split_netmask():
    addr = 'cafe:cafe::/128/190'
    with NetmaskTestMixin_v4.assertAddressError("Only one '/' permitted in %r" % addr):
        NetmaskTestMixin_v4.factory(addr)
    scoped_addr = 'cafe:cafe::%scope/128/190'
    with NetmaskTestMixin_v4.assertAddressError("Only one '/' permitted in %r" % scoped_addr):
        NetmaskTestMixin_v4.factory(scoped_addr)

NetmaskTestMixin_v4 = test_ipaddress.NetmaskTestMixin_v4()
test_split_netmask()
