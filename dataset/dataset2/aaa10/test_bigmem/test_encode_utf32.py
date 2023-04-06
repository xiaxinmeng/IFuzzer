from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_4G // 4 + 5, memuse=test_bigmem.ascii_char_size + test_bigmem.ucs4_char_size + 4)
def test_encode_utf32(StrTest, size):
    try:
        return StrTest.basic_encode_test(size, 'utf32', expectedsize=4 * size + 4)
    except MemoryError:
        pass

StrTest = test_bigmem.StrTest()
test_encode_utf32()
