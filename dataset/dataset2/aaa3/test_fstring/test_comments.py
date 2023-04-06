import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_comments():
    d = {'#': 'hash'}
    TestCase.assertEqual(f"{'#'}", '#')
    TestCase.assertEqual(f"{d['#']}", 'hash')
    TestCase.assertAllRaise(SyntaxError, "f-string expression part cannot include '#'", ["f'{1#}'", "f'{3(#)}'", "f'{#}'"])
    TestCase.assertAllRaise(SyntaxError, "f-string: unmatched '\\)'", ["f'{)#}'"])

TestCase = test_fstring.TestCase()
test_comments()
