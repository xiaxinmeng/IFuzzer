import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_v4_with_v6_scoped_equality():
    for lhs in ComparisonTests.v4_objects:
        for rhs in ComparisonTests.v6_scoped_objects:
            ComparisonTests.assertNotEqual(lhs, rhs)

ComparisonTests = test_ipaddress.ComparisonTests()
test_v4_with_v6_scoped_equality()
