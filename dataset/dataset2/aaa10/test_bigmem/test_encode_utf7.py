from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_4G // 5 + 70, memuse=test_bigmem.ascii_char_size + 8 + 1)
def test_encode_utf7(StrTest, size):
    try:
        return StrTest.basic_encode_test(size, 'utf7')
    except MemoryError:
        pass

StrTest = test_bigmem.StrTest()
test_encode_utf7()
