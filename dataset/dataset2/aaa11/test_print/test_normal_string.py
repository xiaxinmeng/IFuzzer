import unittest
import sys
from io import StringIO
from test import support
import test_print

def test_normal_string():
    python2_print_str = 'print "Hello World"'
    with TestPy2MigrationHint.assertRaises(SyntaxError) as context:
        exec(python2_print_str)
    TestPy2MigrationHint.assertIn('print("Hello World")', str(context.exception))

TestPy2MigrationHint = test_print.TestPy2MigrationHint()
test_normal_string()
