import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_assignment():
    TestCase.assertAllRaise(SyntaxError, 'invalid syntax', ["f'' = 3", "f'{0}' = x", "f'{x}' = x"])

TestCase = test_fstring.TestCase()
test_assignment()
