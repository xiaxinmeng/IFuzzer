import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_curly_brace_after_primary_raises_immediately():
    SyntaxTestCase._check_error('f{', 'invalid syntax', mode='single')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_curly_brace_after_primary_raises_immediately()
