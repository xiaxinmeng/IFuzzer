from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_2G // 5 + 2, memuse=test_bigmem.pointer_size * 5)
def test_count(BaseStrTest, size):
    l = [1, 2, 3, 4, 5] * size
    BaseStrTest.assertEqual(l.count(1), size)
    BaseStrTest.assertEqual(l.count('1'), 0)

BaseStrTest = test_bigmem.BaseStrTest()
test_count()
