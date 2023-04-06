import builtins
import unittest
from test.support import swap_item, swap_attr
import test_dynamic

def test_cannot_replace_builtins_dict_while_active():

    def foo():
        x = range(3)
        yield len(x)
        yield len(x)
    RebindBuiltinsTests.configure_func(foo)
    g = foo()
    RebindBuiltinsTests.assertEqual(next(g), 3)
    with swap_item(globals(), '__builtins__', {'len': lambda x: 7}):
        RebindBuiltinsTests.assertEqual(next(g), 3)

RebindBuiltinsTests = test_dynamic.RebindBuiltinsTests()
test_cannot_replace_builtins_dict_while_active()
