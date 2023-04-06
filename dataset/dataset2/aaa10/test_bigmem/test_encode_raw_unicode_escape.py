from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_4G // 6 + 2, memuse=test_bigmem.ascii_char_size + test_bigmem.ucs4_char_size + 1)
def test_encode_raw_unicode_escape(StrTest, size):
    try:
        return StrTest.basic_encode_test(size, 'raw_unicode_escape')
    except MemoryError:
        pass

StrTest = test_bigmem.StrTest()
test_encode_raw_unicode_escape()
