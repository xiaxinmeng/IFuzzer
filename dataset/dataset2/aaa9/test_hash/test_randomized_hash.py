import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

def test_randomized_hash():
    run1 = HashRandomizationTests.get_hash(HashRandomizationTests.repr_, seed='random')
    run2 = HashRandomizationTests.get_hash(HashRandomizationTests.repr_, seed='random')
    HashRandomizationTests.assertNotEqual(run1, run2)

HashRandomizationTests = test_hash.HashRandomizationTests()

test_randomized_hash()
