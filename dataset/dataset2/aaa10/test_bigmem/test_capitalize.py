from test import support
from test.support import bigmemtest, _1G, _2G, _4G
import unittest
import operator
import sys
import test_bigmem

@bigmemtest(size=_2G, memuse=2)
def test_capitalize(StrTest, size):
    StrTest._test_capitalize(size)

StrTest = test_bigmem.StrTest()
test_capitalize()
