import builtins
import unittest
from test.support import swap_item, swap_attr
import test_dynamic

def test_cannot_replace_builtins_dict_between_calls():

    def foo():
        return len([1, 2, 3])
    RebindBuiltinsTests.configure_func(foo)
    RebindBuiltinsTests.assertEqual(foo(), 3)
    with swap_item(globals(), '__builtins__', {'len': lambda x: 7}):
        RebindBuiltinsTests.assertEqual(foo(), 3)

RebindBuiltinsTests = test_dynamic.RebindBuiltinsTests()
test_cannot_replace_builtins_dict_between_calls()
