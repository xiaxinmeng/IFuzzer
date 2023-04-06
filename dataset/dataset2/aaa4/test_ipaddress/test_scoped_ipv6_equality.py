import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_scoped_ipv6_equality():
    for (lhs, rhs) in zip(ComparisonTests.v6_objects, ComparisonTests.v6_scoped_objects):
        ComparisonTests.assertNotEqual(lhs, rhs)

ComparisonTests = test_ipaddress.ComparisonTests()
test_scoped_ipv6_equality()
