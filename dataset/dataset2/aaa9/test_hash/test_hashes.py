import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

def test_hashes():
    _default_hash = object.__hash__
    for obj in HashBuiltinsTestCase.hashes_to_check:
        HashBuiltinsTestCase.assertEqual(hash(obj), _default_hash(obj))

HashBuiltinsTestCase = test_hash.HashBuiltinsTestCase()
test_hashes()
