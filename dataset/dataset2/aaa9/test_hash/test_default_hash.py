import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

def test_default_hash():
    for obj in HashInheritanceTestCase.default_expected:
        HashInheritanceTestCase.assertEqual(hash(obj), test_hash._default_hash(obj))

HashInheritanceTestCase = test_hash.HashInheritanceTestCase()
test_default_hash()
