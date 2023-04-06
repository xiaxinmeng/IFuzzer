import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_pos_only_call_via_unpacking():

    def f(a, b, /):
        return a + b
    PositionalOnlyTestCase.assertEqual(f(*[1, 2]), 3)

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_pos_only_call_via_unpacking()
