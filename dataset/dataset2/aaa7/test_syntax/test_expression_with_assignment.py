import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_expression_with_assignment():
    SyntaxTestCase._check_error("print(end1 + end2 = ' ')", 'expression cannot contain assignment, perhaps you meant "=="?', offset=19)

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_expression_with_assignment()
