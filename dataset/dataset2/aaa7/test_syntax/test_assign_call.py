import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_assign_call():
    SyntaxTestCase._check_error('f() = 1', 'assign')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_assign_call()
