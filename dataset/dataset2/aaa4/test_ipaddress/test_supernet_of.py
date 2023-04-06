import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_supernet_of():
    NetworkTestCase_v4.assertFalse(NetworkTestCase_v4.factory('2000:999::/56').supernet_of(NetworkTestCase_v4.factory('2000:aaa::/48')))
    NetworkTestCase_v4.assertFalse(NetworkTestCase_v4.factory('2000:aaa::/56').supernet_of(NetworkTestCase_v4.factory('2000:aaa::/48')))
    NetworkTestCase_v4.assertFalse(NetworkTestCase_v4.factory('2000:bbb::/56').supernet_of(NetworkTestCase_v4.factory('2000:aaa::/48')))
    NetworkTestCase_v4.assertTrue(NetworkTestCase_v4.factory('2000:aaa::/48').supernet_of(NetworkTestCase_v4.factory('2000:aaa::/56')))

NetworkTestCase_v4 = test_ipaddress.NetworkTestCase_v4()
test_supernet_of()
