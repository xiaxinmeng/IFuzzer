import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_errors():
    TestCase.assertAllRaise(TypeError, 'unsupported', ["f'{(lambda: 0):x}'", "f'{(0,):x}'"])
    TestCase.assertAllRaise(ValueError, 'Unknown format code', ["f'{1000:j}'", "f'{1000:j}'"])

TestCase = test_fstring.TestCase()
test_errors()
