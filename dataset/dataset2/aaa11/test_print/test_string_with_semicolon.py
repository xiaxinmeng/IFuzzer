import unittest
import sys
from io import StringIO
from test import support
import test_print

def test_string_with_semicolon():
    python2_print_str = 'print p;'
    with TestPy2MigrationHint.assertRaises(SyntaxError) as context:
        exec(python2_print_str)
    TestPy2MigrationHint.assertIn('print(p)', str(context.exception))

TestPy2MigrationHint = test_print.TestPy2MigrationHint()
test_string_with_semicolon()
