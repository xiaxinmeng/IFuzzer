from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_1G - 1, memuse=12)
def test_repeat_large_2(TupleTest, size):
    return TupleTest.basic_test_repeat(size)

TupleTest = test_bigmem.TupleTest()
test_repeat_large_2()
