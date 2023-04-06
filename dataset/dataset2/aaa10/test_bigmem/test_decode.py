from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_2G + 2, memuse=1 + test_bigmem.ascii_char_size)
def test_decode(BytesTest, size):
    s = BytesTest.from_latin1('.') * size
    BytesTest.assertEqual(len(s.decode('utf-8')), size)

BytesTest = test_bigmem.BytesTest()
test_decode()
