import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_bad_outdent():
    SyntaxTestCase._check_error('if 1:\n  foo()\n bar()', 'unindent does not match .* level', subclass=IndentationError)

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_bad_outdent()
