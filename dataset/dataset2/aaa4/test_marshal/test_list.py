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
pointer_size = 8 if sys.maxsize > 0xFFFFFFFF else 4
@support.bigmemtest(size=LARGE_SIZE, memuse=pointer_size + 1, dry_run=False)
def test_list(ContainerTestCase, size):
    ContainerTestCase.check_unmarshallable([None] * size)

ContainerTestCase = test_marshal.ContainerTestCase()
test_list()
