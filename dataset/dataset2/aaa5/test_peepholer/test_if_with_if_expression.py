import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_if_with_if_expression():

    def f(x):
        if True if x else False:
            return True
        return False
    TestTranforms.assertTrue(f(True))
    TestTranforms.check_lnotab(f)

TestTranforms = test_peepholer.TestTranforms()
test_if_with_if_expression()
