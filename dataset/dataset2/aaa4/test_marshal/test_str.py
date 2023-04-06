from test import support
from test.support import os_helper
import array
import io
import marshal
import sys
import unittest
import os
import types
import _testcapi
import test_marshal
LARGE_SIZE = 2**31
@support.bigmemtest(size=LARGE_SIZE, memuse=2, dry_run=False)
def test_str(LargeValuesTestCase, size):
    LargeValuesTestCase.check_unmarshallable('x' * size)

LargeValuesTestCase = test_marshal.LargeValuesTestCase()
test_str()
