import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_make_function_doesnt_bail():

    def f():

        def g() -> 1 + 1:
            pass
        return g
    TestTranforms.assertNotInBytecode(f, 'BINARY_ADD')
    TestTranforms.check_lnotab(f)

TestTranforms = test_peepholer.TestTranforms()
test_make_function_doesnt_bail()
