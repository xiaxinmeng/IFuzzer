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

def test_leading_newlines():
    s256 = ''.join(['\n'] * 256 + ['spam'])
    co = compile(s256, 'fn', 'exec')
    TestSpecifics.assertEqual(co.co_firstlineno, 1)
    TestSpecifics.assertEqual(list(co.co_lines()), [(0, 8, 257)])

TestSpecifics = test_compile.TestSpecifics()
test_leading_newlines()
