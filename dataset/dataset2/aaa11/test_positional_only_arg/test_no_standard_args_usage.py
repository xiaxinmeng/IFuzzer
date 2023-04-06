import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_no_standard_args_usage():

    def f(a, b, /, *, c):
        pass
    f(1, 2, c=3)
    with PositionalOnlyTestCase.assertRaises(TypeError):
        f(1, b=2, c=3)

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_no_standard_args_usage()
