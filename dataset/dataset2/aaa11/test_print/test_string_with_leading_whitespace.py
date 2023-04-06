import unittest
import sys
from io import StringIO
from test import support
import test_print

def test_string_with_leading_whitespace():
    python2_print_str = 'if 1:\n            print "Hello World"\n        '
    with TestPy2MigrationHint.assertRaises(SyntaxError) as context:
        exec(python2_print_str)
    TestPy2MigrationHint.assertIn('print("Hello World")', str(context.exception))

TestPy2MigrationHint = test_print.TestPy2MigrationHint()
test_string_with_leading_whitespace()
