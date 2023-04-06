import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

@test_hash.skip_unless_internalhash
def test_fixed_hash():
    h = HashInheritanceTestCase.get_expected_hash(1, 3)
    HashInheritanceTestCase.assertEqual(HashInheritanceTestCase.get_hash(HashInheritanceTestCase.repr_, seed=42), h)

HashInheritanceTestCase = test_hash.HashInheritanceTestCase()
HashInheritanceTestCase.setUp()
test_fixed_hash()
