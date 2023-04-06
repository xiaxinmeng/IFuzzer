import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

def test_not_hashable():
    for obj in HashInheritanceTestCase.error_expected:
        HashInheritanceTestCase.assertNotIsInstance(obj, Hashable)

HashInheritanceTestCase = test_hash.HashInheritanceTestCase()
test_not_hashable()
