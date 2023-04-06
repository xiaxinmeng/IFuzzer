import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_condition_with_binop_with_bools():

    def f():
        if True or False:
            return 1
        return 0
    TestTranforms.assertEqual(f(), 1)
    TestTranforms.check_lnotab(f)

TestTranforms = test_peepholer.TestTranforms()
test_condition_with_binop_with_bools()
