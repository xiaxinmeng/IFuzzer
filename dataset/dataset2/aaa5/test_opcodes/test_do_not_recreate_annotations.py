import unittest
from test import ann_module, support
import test_opcodes

def test_do_not_recreate_annotations():
    with support.swap_item(globals(), '__annotations__', {}):
        del globals()['__annotations__']

        class C:
            del __annotations__
            with OpcodeTest.assertRaises(NameError):
                x: int

OpcodeTest = test_opcodes.OpcodeTest()
test_do_not_recreate_annotations()
