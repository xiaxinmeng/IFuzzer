import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_invalid_fstring_conversion():
    UnparseTestCase.check_invalid(ast.FormattedValue(value=ast.Constant(value='a', kind=None), conversion=ord('Y'), format_spec=None))

UnparseTestCase = test_unparse.UnparseTestCase()
test_invalid_fstring_conversion()
