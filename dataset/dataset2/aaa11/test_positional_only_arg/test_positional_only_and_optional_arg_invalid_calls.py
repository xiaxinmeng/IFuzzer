import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_positional_only_and_optional_arg_invalid_calls():

    def f(a, b, /, c=3):
        pass
    f(1, 2)
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, "f\\(\\) missing 1 required positional argument: 'b'"):
        f(1)
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, "f\\(\\) missing 2 required positional arguments: 'a' and 'b'"):
        f()
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, 'f\\(\\) takes from 2 to 3 positional arguments but 4 were given'):
        f(1, 2, 3, 4)

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_positional_only_and_optional_arg_invalid_calls()
