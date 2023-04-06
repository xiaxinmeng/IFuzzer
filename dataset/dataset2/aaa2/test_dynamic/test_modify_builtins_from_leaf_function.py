import builtins
import unittest
from test.support import swap_item, swap_attr
import test_dynamic

def test_modify_builtins_from_leaf_function():
    with swap_attr(builtins, 'len', len):

        def bar():
            builtins.len = lambda x: 4

        def foo(modifier):
            l = []
            l.append(len(range(7)))
            modifier()
            l.append(len(range(7)))
            return l
        RebindBuiltinsTests.configure_func(foo, lambda : None)
        RebindBuiltinsTests.assertEqual(foo(bar), [7, 4])

RebindBuiltinsTests = test_dynamic.RebindBuiltinsTests()
test_modify_builtins_from_leaf_function()
