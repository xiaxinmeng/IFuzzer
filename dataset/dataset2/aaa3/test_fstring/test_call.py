import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_call():

    def foo(x):
        return 'x=' + str(x)
    TestCase.assertEqual(f'{foo(10)}', 'x=10')

TestCase = test_fstring.TestCase()
test_call()
