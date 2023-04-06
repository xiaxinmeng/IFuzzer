import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_kwargs_last2():
    SyntaxTestCase._check_error("int(**{'base': 10}, '2')", 'positional argument follows keyword argument unpacking')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_kwargs_last2()
