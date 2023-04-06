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

def test_string():
    for s in ['', 'Andrè Previn', 'abc', ' ' * 10000]:
        StringTestCase.helper(s)

StringTestCase = test_marshal.StringTestCase()
test_string()
