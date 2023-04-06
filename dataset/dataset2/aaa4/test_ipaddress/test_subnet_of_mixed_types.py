import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_subnet_of_mixed_types():
    with NetworkTestCase_v4.assertRaises(TypeError):
        ipaddress.IPv4Network('10.0.0.0/30').supernet_of(ipaddress.IPv6Network('::1/128'))
    with NetworkTestCase_v4.assertRaises(TypeError):
        ipaddress.IPv6Network('::1/128').supernet_of(ipaddress.IPv4Network('10.0.0.0/30'))
    with NetworkTestCase_v4.assertRaises(TypeError):
        ipaddress.IPv4Network('10.0.0.0/30').subnet_of(ipaddress.IPv6Network('::1/128'))
    with NetworkTestCase_v4.assertRaises(TypeError):
        ipaddress.IPv6Network('::1/128').subnet_of(ipaddress.IPv4Network('10.0.0.0/30'))

NetworkTestCase_v4 = test_ipaddress.NetworkTestCase_v4()
test_subnet_of_mixed_types()
