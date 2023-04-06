import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_floats_rejected():
    with CommonTestMixin.assertAddressError(re.escape(repr('1.0'))):
        CommonTestMixin.factory(1.0)

CommonTestMixin = test_ipaddress.CommonTestMixin()
test_floats_rejected()
