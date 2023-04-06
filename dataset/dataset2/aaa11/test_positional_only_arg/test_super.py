import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_super():
    sentinel = object()

    class A:

        def method(PositionalOnlyTestCase):
            return sentinel

    class C(A):

        def method(PositionalOnlyTestCase, /):
            return super().method()
    PositionalOnlyTestCase.assertEqual(C().method(), sentinel)

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_super()
