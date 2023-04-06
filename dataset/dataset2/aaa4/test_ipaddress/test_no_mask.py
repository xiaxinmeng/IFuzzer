import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_no_mask():
    for address in ('::1', 1, b'\x00' * 15 + b'\x01'):
        net = NetmaskTestMixin_v4.factory(address)
        NetmaskTestMixin_v4.assertEqual(str(net), '::1/128')
        NetmaskTestMixin_v4.assertEqual(str(net.netmask), 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')
        NetmaskTestMixin_v4.assertEqual(str(net.hostmask), '::')
    scoped_net = NetmaskTestMixin_v4.factory('::1%scope')
    NetmaskTestMixin_v4.assertEqual(str(scoped_net), '::1%scope/128')
    NetmaskTestMixin_v4.assertEqual(str(scoped_net.netmask), 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')
    NetmaskTestMixin_v4.assertEqual(str(scoped_net.hostmask), '::')

NetmaskTestMixin_v4 = test_ipaddress.NetmaskTestMixin_v4()
test_no_mask()
