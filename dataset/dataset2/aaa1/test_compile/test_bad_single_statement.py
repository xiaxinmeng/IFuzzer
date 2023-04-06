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

def test_bad_single_statement():
    TestSpecifics.assertInvalidSingle('1\n2')
    TestSpecifics.assertInvalidSingle('def f(): pass')
    TestSpecifics.assertInvalidSingle('a = 13\nb = 187')
    TestSpecifics.assertInvalidSingle('del x\ndel y')
    TestSpecifics.assertInvalidSingle('f()\ng()')
    TestSpecifics.assertInvalidSingle('f()\n# blah\nblah()')
    TestSpecifics.assertInvalidSingle('f()\nxy # blah\nblah()')
    TestSpecifics.assertInvalidSingle('x = 5 # comment\nx = 6\n')

TestSpecifics = test_compile.TestSpecifics()
test_bad_single_statement()
