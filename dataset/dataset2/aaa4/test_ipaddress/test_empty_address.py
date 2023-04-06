import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_empty_address():
    with CommonTestMixin.assertAddressError('Address cannot be empty'):
        CommonTestMixin.factory('')

CommonTestMixin = test_ipaddress.CommonTestMixin()
test_empty_address()
