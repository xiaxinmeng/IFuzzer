import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

@test_hash.skip_unless_internalhash
def test_long_fixed_hash():
    if StringlikeHashRandomizationTests.repr_long is None:
        return
    h = StringlikeHashRandomizationTests.get_expected_hash(2, 11)
    StringlikeHashRandomizationTests.assertEqual(StringlikeHashRandomizationTests.get_hash(StringlikeHashRandomizationTests.repr_long, seed=42), h)

StringlikeHashRandomizationTests = test_hash.StringlikeHashRandomizationTests()
test_long_fixed_hash()
