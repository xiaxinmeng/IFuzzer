import unittest
import sys
from io import StringIO
from test import support
import test_print

def test_string_in_loop_on_same_line():
    python2_print_str = 'for i in s: print i'
    with TestPy2MigrationHint.assertRaises(SyntaxError) as context:
        exec(python2_print_str)
    TestPy2MigrationHint.assertIn('print(i)', str(context.exception))

TestPy2MigrationHint = test_print.TestPy2MigrationHint()
test_string_in_loop_on_same_line()
