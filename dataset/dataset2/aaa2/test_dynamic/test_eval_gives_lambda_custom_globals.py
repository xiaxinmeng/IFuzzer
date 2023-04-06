import builtins
import unittest
from test.support import swap_item, swap_attr
import test_dynamic

def test_eval_gives_lambda_custom_globals():
    globals_dict = {'len': lambda x: 7}
    foo = eval('lambda: len([])', globals_dict)
    RebindBuiltinsTests.configure_func(foo)
    RebindBuiltinsTests.assertEqual(foo(), 7)

RebindBuiltinsTests = test_dynamic.RebindBuiltinsTests()
test_eval_gives_lambda_custom_globals()
