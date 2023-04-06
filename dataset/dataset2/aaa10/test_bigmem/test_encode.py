from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_2G + 2, memuse=test_bigmem.ascii_char_size + 1)
def test_encode(StrTest, size):
    return StrTest.basic_encode_test(size, 'utf-8')

StrTest = test_bigmem.StrTest()
test_encode()
