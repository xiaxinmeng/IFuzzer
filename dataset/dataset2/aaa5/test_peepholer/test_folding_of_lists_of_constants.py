import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_folding_of_lists_of_constants():
    for (line, elem) in (('a in [1,2,3]', (1, 2, 3)), ('a not in ["a","b","c"]', ('a', 'b', 'c')), ('a in [None, 1, None]', (None, 1, None)), ('a not in [(1, 2), 3, 4]', ((1, 2), 3, 4))):
        code = compile(line, '', 'single')
        TestTranforms.assertInBytecode(code, 'LOAD_CONST', elem)
        TestTranforms.assertNotInBytecode(code, 'BUILD_LIST')
        TestTranforms.check_lnotab(code)

TestTranforms = test_peepholer.TestTranforms()
test_folding_of_lists_of_constants()
