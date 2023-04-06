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

@support.cpython_only
def test_same_filename_used():
    s = 'def f(): pass\ndef g(): pass'
    co = compile(s, 'myfile', 'exec')
    co = marshal.loads(marshal.dumps(co))
    for obj in co.co_consts:
        if isinstance(obj, types.CodeType):
            CodeTestCase.assertIs(co.co_filename, obj.co_filename)

CodeTestCase = test_marshal.CodeTestCase()
test_same_filename_used()
