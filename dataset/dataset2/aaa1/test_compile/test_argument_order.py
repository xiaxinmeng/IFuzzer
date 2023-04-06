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

def test_argument_order():
    TestSpecifics.assertRaises(SyntaxError, exec, 'def f(a=1, b): pass')

TestSpecifics = test_compile.TestSpecifics()
test_argument_order()
