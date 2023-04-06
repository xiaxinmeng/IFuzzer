import datetime
import os
import sys
import unittest
from test.support.script_helper import assert_python_ok
from collections.abc import Hashable
import test_hash

def test_hashable():
    objects = HashInheritanceTestCase.default_expected + HashInheritanceTestCase.fixed_expected
    for obj in objects:
        HashInheritanceTestCase.assertIsInstance(obj, Hashable)

HashInheritanceTestCase = test_hash.HashInheritanceTestCase()
test_hashable()
