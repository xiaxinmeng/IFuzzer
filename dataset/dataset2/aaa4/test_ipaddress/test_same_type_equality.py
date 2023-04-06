import unittest
import re
import contextlib
import operator
import pickle
import ipaddress
import weakref
from test.support import LARGEST, SMALLEST
import test_ipaddress

def test_same_type_equality():
    for obj in ComparisonTests.objects_with_scoped:
        ComparisonTests.assertEqual(obj, obj)
        ComparisonTests.assertLessEqual(obj, obj)
        ComparisonTests.assertGreaterEqual(obj, obj)

ComparisonTests = test_ipaddress.ComparisonTests()
test_same_type_equality()
