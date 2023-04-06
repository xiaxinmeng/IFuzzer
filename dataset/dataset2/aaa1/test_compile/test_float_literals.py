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

def test_float_literals():
    TestSpecifics.assertRaises(SyntaxError, eval, '2e')
    TestSpecifics.assertRaises(SyntaxError, eval, '2.0e+')
    TestSpecifics.assertRaises(SyntaxError, eval, '1e-')
    TestSpecifics.assertRaises(SyntaxError, eval, '3-4e/21')

TestSpecifics = test_compile.TestSpecifics()
test_float_literals()
