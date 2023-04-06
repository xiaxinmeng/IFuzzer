from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_2G // 2 + 2, memuse=test_bigmem.pointer_size * 2 * 9 / 8)
def test_extend_small(ListTest, size):
    return ListTest.basic_test_extend(size)

ListTest = test_bigmem.ListTest()
test_extend_small()
