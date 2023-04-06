from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_2G + 2, memuse=test_bigmem.pointer_size + test_bigmem.ascii_char_size * 7)
def test_repr_large(StrTest, size):
    return StrTest.basic_test_repr(size)

StrTest = test_bigmem.StrTest()
StrTest.setUp()
test_repr_large()
