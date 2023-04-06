import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_unot():

    def unot(x):
        if not x == 2:
            del x
    TestTranforms.assertNotInBytecode(unot, 'UNARY_NOT')
    TestTranforms.assertNotInBytecode(unot, 'POP_JUMP_IF_FALSE')
    TestTranforms.assertInBytecode(unot, 'POP_JUMP_IF_TRUE')
    TestTranforms.check_lnotab(unot)

TestTranforms = test_peepholer.TestTranforms()
test_unot()
