import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_global_param_err_first():
    source = 'if 1:\n            def error(a):\n                global a  # SyntaxError\n            def error2():\n                b = 1\n                global b  # SyntaxError\n            '
    SyntaxTestCase._check_error(source, 'parameter and global', lineno=3)

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_global_param_err_first()
