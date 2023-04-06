import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

def test_coerced_floats():
    HashEqualityTestCase.same_hash(int(1.23e+300), float(1.23e+300))
    HashEqualityTestCase.same_hash(float(0.5), complex(0.5, 0.0))

HashEqualityTestCase = test_hash.HashEqualityTestCase()
test_coerced_floats()
