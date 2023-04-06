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

def test_single_statement():
    TestSpecifics.compile_single('1 + 2')
    TestSpecifics.compile_single('\n1 + 2')
    TestSpecifics.compile_single('1 + 2\n')
    TestSpecifics.compile_single('1 + 2\n\n')
    TestSpecifics.compile_single('1 + 2\t\t\n')
    TestSpecifics.compile_single('1 + 2\t\t\n        ')
    TestSpecifics.compile_single('1 + 2 # one plus two')
    TestSpecifics.compile_single('1; 2')
    TestSpecifics.compile_single('import sys; sys')
    TestSpecifics.compile_single('def f():\n   pass')
    TestSpecifics.compile_single('while False:\n   pass')
    TestSpecifics.compile_single('if x:\n   f(x)')
    TestSpecifics.compile_single('if x:\n   f(x)\nelse:\n   g(x)')
    TestSpecifics.compile_single('class T:\n   pass')

TestSpecifics = test_compile.TestSpecifics()
test_single_statement()
