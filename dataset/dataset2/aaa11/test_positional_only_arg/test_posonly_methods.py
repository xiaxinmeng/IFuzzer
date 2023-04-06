import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_posonly_methods():

    class Example:

        def f(PositionalOnlyTestCase, a, b, /):
            return (a, b)
    PositionalOnlyTestCase.assertEqual(Example().f(1, 2), (1, 2))
    PositionalOnlyTestCase.assertEqual(Example.f(Example(), 1, 2), (1, 2))
    PositionalOnlyTestCase.assertRaises(TypeError, Example.f, 1, 2)
    expected = "f\\(\\) got some positional-only arguments passed as keyword arguments: 'b'"
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, expected):
        Example().f(1, b=2)

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_posonly_methods()
