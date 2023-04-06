import unittest
from test import ann_module, support
import test_opcodes

def test_no_annotations_if_not_needed():

    class C:
        pass
    with OpcodeTest.assertRaises(AttributeError):
        C.__annotations__

OpcodeTest = test_opcodes.OpcodeTest()
test_no_annotations_if_not_needed()
