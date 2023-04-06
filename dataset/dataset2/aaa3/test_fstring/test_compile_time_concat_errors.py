import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_compile_time_concat_errors():
    TestCase.assertAllRaise(SyntaxError, 'cannot mix bytes and nonbytes literals', ["f'' b''", "b'' f''"])

TestCase = test_fstring.TestCase()
test_compile_time_concat_errors()
