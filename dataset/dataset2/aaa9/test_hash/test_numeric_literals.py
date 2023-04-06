import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

def test_numeric_literals():
    HashEqualityTestCase.same_hash(1, 1, 1.0, 1.0 + 0j)
    HashEqualityTestCase.same_hash(0, 0.0, 0.0 + 0j)
    HashEqualityTestCase.same_hash(-1, -1.0, -1.0 + 0j)
    HashEqualityTestCase.same_hash(-2, -2.0, -2.0 + 0j)

HashEqualityTestCase = test_hash.HashEqualityTestCase()
test_numeric_literals()
