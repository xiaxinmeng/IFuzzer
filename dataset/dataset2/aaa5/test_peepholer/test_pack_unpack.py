import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_pack_unpack():
    for (line, elem) in (('a, = a,', 'LOAD_CONST'), ('a, b = a, b', 'ROT_TWO'), ('a, b, c = a, b, c', 'ROT_THREE')):
        code = compile(line, '', 'single')
        TestTranforms.assertInBytecode(code, elem)
        TestTranforms.assertNotInBytecode(code, 'BUILD_TUPLE')
        TestTranforms.assertNotInBytecode(code, 'UNPACK_TUPLE')
        TestTranforms.check_lnotab(code)

TestTranforms = test_peepholer.TestTranforms()
test_pack_unpack()
