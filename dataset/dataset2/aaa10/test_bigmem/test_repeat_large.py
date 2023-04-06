from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_2G + 2, memuse=test_bigmem.pointer_size * 3)
def test_repeat_large(TupleTest, size):
    return TupleTest.basic_test_repeat(size)

TupleTest = test_bigmem.TupleTest()
test_repeat_large()
