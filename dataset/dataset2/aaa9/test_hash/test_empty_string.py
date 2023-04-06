import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

@test_hash.skip_unless_internalhash
def test_empty_string():
    StrHashRandomizationTests.assertEqual(hash(memoryview(b'')), 0)

StrHashRandomizationTests = test_hash.StrHashRandomizationTests()
test_empty_string()
