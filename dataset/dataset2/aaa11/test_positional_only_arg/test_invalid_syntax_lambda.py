import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_invalid_syntax_lambda():
    check_syntax_error(PositionalOnlyTestCase, 'lambda a, b = 5, /, c: None', 'non-default argument follows default argument')
    check_syntax_error(PositionalOnlyTestCase, 'lambda a = 5, b, /, c: None', 'non-default argument follows default argument')
    check_syntax_error(PositionalOnlyTestCase, 'lambda a = 5, b, /: None', 'non-default argument follows default argument')
    check_syntax_error(PositionalOnlyTestCase, 'lambda *args, /: None')
    check_syntax_error(PositionalOnlyTestCase, 'lambda *args, a, /: None')
    check_syntax_error(PositionalOnlyTestCase, 'lambda **kwargs, /: None')
    check_syntax_error(PositionalOnlyTestCase, 'lambda /, a = 1: None')
    check_syntax_error(PositionalOnlyTestCase, 'lambda /, a: None')
    check_syntax_error(PositionalOnlyTestCase, 'lambda /: None')
    check_syntax_error(PositionalOnlyTestCase, 'lambda *, a, /: None')
    check_syntax_error(PositionalOnlyTestCase, 'lambda *, /, a: None')
    check_syntax_error(PositionalOnlyTestCase, 'lambda a, /, a: None', "duplicate argument 'a' in function definition")
    check_syntax_error(PositionalOnlyTestCase, 'lambda a, /, *, a: None', "duplicate argument 'a' in function definition")
    check_syntax_error(PositionalOnlyTestCase, 'lambda a, /, b, /: None')
    check_syntax_error(PositionalOnlyTestCase, 'lambda a, /, b, /, c: None')
    check_syntax_error(PositionalOnlyTestCase, 'lambda a, /, b, /, c, *, d: None')
    check_syntax_error(PositionalOnlyTestCase, 'lambda a, *, b, /, c: None')

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_invalid_syntax_lambda()
