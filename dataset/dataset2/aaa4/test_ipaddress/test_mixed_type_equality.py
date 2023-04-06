import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_mixed_type_equality():
    for lhs in ComparisonTests.objects:
        for rhs in ComparisonTests.objects:
            if lhs is rhs:
                continue
            ComparisonTests.assertNotEqual(lhs, rhs)

ComparisonTests = test_ipaddress.ComparisonTests()
test_mixed_type_equality()
