import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_kwargs_last3():
    SyntaxTestCase._check_error("int(**{'base': 10}, *['2'])", 'iterable argument unpacking follows keyword argument unpacking')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_kwargs_last3()
