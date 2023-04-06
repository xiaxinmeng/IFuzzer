import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_empty_line_after_linecont():
    s = '\\\npass\n        \\\n\npass\n'
    try:
        compile(s, '<string>', 'exec')
    except SyntaxError:
        SyntaxTestCase.fail('Empty line after a line continuation character is valid.')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_empty_line_after_linecont()
