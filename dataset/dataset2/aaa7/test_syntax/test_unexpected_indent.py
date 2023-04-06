import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_unexpected_indent():
    SyntaxTestCase._check_error('foo()\n bar()\n', 'unexpected indent', subclass=IndentationError)

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_unexpected_indent()
