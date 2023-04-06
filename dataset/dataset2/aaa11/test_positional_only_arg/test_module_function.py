import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def global_pos_only_f(a, b, /):
    return a, b


def test_module_function():
    with PositionalOnlyTestCase.assertRaisesRegex(TypeError, "f\\(\\) missing 2 required positional arguments: 'a' and 'b'"):
        global_pos_only_f()

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_module_function()
