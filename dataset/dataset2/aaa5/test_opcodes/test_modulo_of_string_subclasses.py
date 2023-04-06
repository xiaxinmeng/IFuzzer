import unittest
from test import ann_module, support
import test_opcodes

def test_modulo_of_string_subclasses():

    class MyString(str):

        def __mod__(OpcodeTest, value):
            return 42
    OpcodeTest.assertEqual(MyString() % 3, 42)

OpcodeTest = test_opcodes.OpcodeTest()
test_modulo_of_string_subclasses()
