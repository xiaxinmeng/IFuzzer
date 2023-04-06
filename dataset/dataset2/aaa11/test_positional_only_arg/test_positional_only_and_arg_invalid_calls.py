import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_positional_only_and_arg_invalid_calls():

    def f(a, b, /, c):
        pass
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, "f\\(\\) missing 1 required positional argument: 'c'"):
        f(1, 2)
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, "f\\(\\) missing 2 required positional arguments: 'b' and 'c'"):
        f(1)
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, "f\\(\\) missing 3 required positional arguments: 'a', 'b', and 'c'"):
        f()
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, 'f\\(\\) takes 3 positional arguments but 4 were given'):
        f(1, 2, 3, 4)

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_positional_only_and_arg_invalid_calls()
