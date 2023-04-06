import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_positional_only_with_optional_invalid_calls():

    def f(a, b=2, /):
        pass
    f(1)
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, "f\\(\\) missing 1 required positional argument: 'a'"):
        f()
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, 'f\\(\\) takes from 1 to 2 positional arguments but 3 were given'):
        f(1, 2, 3)

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_positional_only_with_optional_invalid_calls()
