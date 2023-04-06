import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_while_one():

    def f():
        while 1:
            pass
        return list
    for elem in ('LOAD_CONST', 'POP_JUMP_IF_FALSE'):
        TestTranforms.assertNotInBytecode(f, elem)
    for elem in ('JUMP_ABSOLUTE',):
        TestTranforms.assertInBytecode(f, elem)
    TestTranforms.check_lnotab(f)

TestTranforms = test_peepholer.TestTranforms()
test_while_one()
