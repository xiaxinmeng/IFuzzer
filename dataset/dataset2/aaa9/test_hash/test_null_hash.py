import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

def test_null_hash():
    known_hash_of_obj = StringlikeHashRandomizationTests.get_expected_hash(0, 3)
    StringlikeHashRandomizationTests.assertNotEqual(StringlikeHashRandomizationTests.get_hash(StringlikeHashRandomizationTests.repr_), known_hash_of_obj)
    StringlikeHashRandomizationTests.assertEqual(StringlikeHashRandomizationTests.get_hash(StringlikeHashRandomizationTests.repr_, seed=0), known_hash_of_obj)

StringlikeHashRandomizationTests = test_hash.StringlikeHashRandomizationTests()
test_null_hash()
