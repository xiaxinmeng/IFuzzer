import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_elim_jump_to_uncond_jump():

    def f():
        if a:
            if c or d:
                foo()
        else:
            baz()
    TestTranforms.check_jump_targets(f)
    TestTranforms.check_lnotab(f)

TestTranforms = test_peepholer.TestTranforms()
test_elim_jump_to_uncond_jump()
