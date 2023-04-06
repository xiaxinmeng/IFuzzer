import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_side_effect_order():

    class X:

        def __init__(TestCase):
            TestCase.i = 0

        def __format__(TestCase, spec):
            TestCase.i += 1
            return str(TestCase.i)
    x = X()
    TestCase.assertEqual(f'{x} {x}', '1 2')

TestCase = test_fstring.TestCase()
test_side_effect_order()
