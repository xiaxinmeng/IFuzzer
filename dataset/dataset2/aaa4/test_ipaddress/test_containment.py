import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_containment():
    for obj in ComparisonTests.v4_addresses:
        ComparisonTests.assertIn(obj, ComparisonTests.v4net)
    for obj in ComparisonTests.v6_addresses + ComparisonTests.v6_scoped_addresses:
        ComparisonTests.assertIn(obj, ComparisonTests.v6net)
    for obj in ComparisonTests.v6_addresses + ComparisonTests.v6_scoped_addresses:
        ComparisonTests.assertIn(obj, ComparisonTests.v6net_scoped)
    for obj in ComparisonTests.v4_objects + [ComparisonTests.v6net, ComparisonTests.v6net_scoped]:
        ComparisonTests.assertNotIn(obj, ComparisonTests.v6net)
    for obj in ComparisonTests.v4_objects + [ComparisonTests.v6net, ComparisonTests.v6net_scoped]:
        ComparisonTests.assertNotIn(obj, ComparisonTests.v6net_scoped)
    for obj in ComparisonTests.v6_objects + ComparisonTests.v6_scoped_objects + [ComparisonTests.v4net]:
        ComparisonTests.assertNotIn(obj, ComparisonTests.v4net)

ComparisonTests = test_ipaddress.ComparisonTests()
test_containment()
