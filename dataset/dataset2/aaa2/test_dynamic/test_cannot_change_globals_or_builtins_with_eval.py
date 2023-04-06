import builtins
import unittest
from test.support import swap_item, swap_attr
import test_dynamic

def test_cannot_change_globals_or_builtins_with_eval():

    def foo():
        return len([1, 2, 3])
    RebindBuiltinsTests.configure_func(foo)
    builtins_dict = {'len': lambda x: 7}
    globals_dict = {'foo': foo, '__builtins__': builtins_dict, 'len': lambda x: 8}
    RebindBuiltinsTests.assertEqual(eval('foo()', globals_dict), 3)
    RebindBuiltinsTests.assertEqual(eval('foo()', {'foo': foo}), 3)

RebindBuiltinsTests = test_dynamic.RebindBuiltinsTests()
test_cannot_change_globals_or_builtins_with_eval()
