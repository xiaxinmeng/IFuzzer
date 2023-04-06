import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_no_indent():
    SyntaxTestCase._check_error('if 1:\nfoo()', 'expected an indented block', subclass=IndentationError)

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_no_indent()
