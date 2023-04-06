import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_invalid_line_continuation_left_recursive():
    SyntaxTestCase._check_error('A.Ɗ\\ ', 'unexpected character after line continuation character')
    SyntaxTestCase._check_error('A.μ\\\n', 'unexpected EOF while parsing')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_invalid_line_continuation_left_recursive()
