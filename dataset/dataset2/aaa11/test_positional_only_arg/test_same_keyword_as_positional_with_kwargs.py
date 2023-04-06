import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_same_keyword_as_positional_with_kwargs():

    def f(something, /, **kwargs):
        return (something, kwargs)
    PositionalOnlyTestCase.assertEqual(f(42, something=42), (42, {'something': 42}))
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, "f\\(\\) missing 1 required positional argument: 'something'"):
        f(something=42)
    PositionalOnlyTestCase.assertEqual(f(42), (42, {}))

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_same_keyword_as_positional_with_kwargs()
