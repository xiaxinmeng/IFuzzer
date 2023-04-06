import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

def test_error_hash():
    for obj in HashInheritanceTestCase.error_expected:
        HashInheritanceTestCase.assertRaises(TypeError, hash, obj)

HashInheritanceTestCase = test_hash.HashInheritanceTestCase()
test_error_hash()
