import builtins
import unittest
from test.support import swap_item, swap_attr
import test_dynamic

def test_modify_builtins():

    def foo():
        return len([1, 2, 3])
    RebindBuiltinsTests.configure_func(foo)
    RebindBuiltinsTests.assertEqual(foo(), 3)
    with swap_attr(builtins, 'len', lambda x: 7):
        RebindBuiltinsTests.assertEqual(foo(), 7)

RebindBuiltinsTests = test_dynamic.RebindBuiltinsTests()
test_modify_builtins()
