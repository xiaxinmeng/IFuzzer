import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

@test_hash.skip_unless_internalhash
def test_ucs2_string():
    h = StrHashRandomizationTests.get_expected_hash(3, 6)
    StrHashRandomizationTests.assertEqual(StrHashRandomizationTests.get_hash(StrHashRandomizationTests.repr_ucs2, seed=0), h)
    h = StrHashRandomizationTests.get_expected_hash(4, 6)
    StrHashRandomizationTests.assertEqual(StrHashRandomizationTests.get_hash(StrHashRandomizationTests.repr_ucs2, seed=42), h)

StrHashRandomizationTests = test_hash.StrHashRandomizationTests()
test_ucs2_string()
