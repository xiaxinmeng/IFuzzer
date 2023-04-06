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

def test_many_codeobjects():
    count = 5000
    codes = (test_marshal.ExceptionTestCase.test_exceptions.__code__,) * count
    marshal.loads(marshal.dumps(codes))

CodeTestCase = test_marshal.CodeTestCase()
test_many_codeobjects()
