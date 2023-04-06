import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_constant_folding():
    exprs = ['3 * -5', '-3 * 5', '2 * (3 * 4)', '(2 * 3) * 4', '(-1, 2, 3)', '(1, -2, 3)', '(1, 2, -3)', '(1, 2, -3) * 6', 'lambda x: x in {(3 * -5) + (-1 - 6), (1, -2, 3) * 2, None}']
    for e in exprs:
        code = compile(e, '', 'single')
        for instr in dis.get_instructions(code):
            TestTranforms.assertFalse(instr.opname.startswith('UNARY_'))
            TestTranforms.assertFalse(instr.opname.startswith('BINARY_'))
            TestTranforms.assertFalse(instr.opname.startswith('BUILD_'))
        TestTranforms.check_lnotab(code)

TestTranforms = test_peepholer.TestTranforms()
test_constant_folding()
