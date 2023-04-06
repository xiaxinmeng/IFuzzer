import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_pos_only_definition():

    def f(a, b, c, /, d, e=1, *, f, g=2):
        pass
    PositionalOnlyTestCase.assertEqual(5, f.__code__.co_argcount)
    PositionalOnlyTestCase.assertEqual(3, f.__code__.co_posonlyargcount)
    PositionalOnlyTestCase.assertEqual((1,), f.__defaults__)

    def f(a, b, c=1, /, d=2, e=3, *, f, g=4):
        pass
    PositionalOnlyTestCase.assertEqual(5, f.__code__.co_argcount)
    PositionalOnlyTestCase.assertEqual(3, f.__code__.co_posonlyargcount)
    PositionalOnlyTestCase.assertEqual((1, 2, 3), f.__defaults__)

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_pos_only_definition()
