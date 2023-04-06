import unittest
import sys
from io import StringIO
from test import support
import test_print

def test_string_with_soft_space():
    python2_print_str = 'print "Hello World",'
    with TestPy2MigrationHint.assertRaises(SyntaxError) as context:
        exec(python2_print_str)
    TestPy2MigrationHint.assertIn('print("Hello World", end=" ")', str(context.exception))

TestPy2MigrationHint = test_print.TestPy2MigrationHint()
test_string_with_soft_space()
