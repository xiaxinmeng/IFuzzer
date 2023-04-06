import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_trailing_nops():

    def f(x):
        while 1:
            return 3
        while 1:
            return 5
        return 6
    TestTranforms.check_lnotab(f)

TestTranforms = test_peepholer.TestTranforms()
test_trailing_nops()
