import dis
import math
import os
import unittest
import sys
import _ast
import tempfile
import types
from test import support
from test.support import script_helper
from test.support.os_helper import FakePath
import builtins

import dis, io
import test_compile

@support.cpython_only
def test_same_filename_used():
    s = 'def f(): pass\ndef g(): pass'
    c = compile(s, 'myfile', 'exec')
    for obj in c.co_consts:
        if isinstance(obj, types.CodeType):
            TestSpecifics.assertIs(obj.co_filename, c.co_filename)

TestSpecifics = test_compile.TestSpecifics()
test_same_filename_used()
