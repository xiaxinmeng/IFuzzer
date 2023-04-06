import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_barry_as_flufl_with_syntax_errors():
    code = '\ndef func1():\n    if a != b:\n        raise ValueError\n\ndef func2():\n    try\n        return 1\n    finally:\n        pass\n'
    SyntaxTestCase._check_error(code, 'invalid syntax')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_barry_as_flufl_with_syntax_errors()
