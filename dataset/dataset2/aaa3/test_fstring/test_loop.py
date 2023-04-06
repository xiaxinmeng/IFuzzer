import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_loop():
    for i in range(1000):
        TestCase.assertEqual(f'i:{i}', 'i:' + str(i))

TestCase = test_fstring.TestCase()
test_loop()
