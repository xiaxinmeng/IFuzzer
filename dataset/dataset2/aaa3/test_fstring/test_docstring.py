import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_docstring():

    def f():
        f'Not a docstring'
    TestCase.assertIsNone(f.__doc__)

    def g():
        f'Not a docstring'
    TestCase.assertIsNone(g.__doc__)

TestCase = test_fstring.TestCase()
test_docstring()
