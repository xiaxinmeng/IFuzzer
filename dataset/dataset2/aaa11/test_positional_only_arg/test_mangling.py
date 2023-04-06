import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_mangling():

    class X:

        def f(PositionalOnlyTestCase, __a=42, /):
            return __a

        def f2(PositionalOnlyTestCase, __a=42, /, __b=43):
            return (__a, __b)

        def f3(PositionalOnlyTestCase, __a=42, /, __b=43, *, __c=44):
            return (__a, __b, __c)
    PositionalOnlyTestCase.assertEqual(X().f(), 42)
    PositionalOnlyTestCase.assertEqual(X().f2(), (42, 43))
    PositionalOnlyTestCase.assertEqual(X().f3(), (42, 43, 44))

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_mangling()
