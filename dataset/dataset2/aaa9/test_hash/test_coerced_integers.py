import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

def test_coerced_integers():
    HashEqualityTestCase.same_hash(int(1), int(1), float(1), complex(1), int('1'), float('1.0'))
    HashEqualityTestCase.same_hash(int(-2 ** 31), float(-2 ** 31))
    HashEqualityTestCase.same_hash(int(1 - 2 ** 31), float(1 - 2 ** 31))
    HashEqualityTestCase.same_hash(int(2 ** 31 - 1), float(2 ** 31 - 1))
    HashEqualityTestCase.same_hash(int(2 ** 31), float(2 ** 31))
    HashEqualityTestCase.same_hash(int(-2 ** 63), float(-2 ** 63))
    HashEqualityTestCase.same_hash(int(2 ** 63), float(2 ** 63))

HashEqualityTestCase = test_hash.HashEqualityTestCase()
test_coerced_integers()
