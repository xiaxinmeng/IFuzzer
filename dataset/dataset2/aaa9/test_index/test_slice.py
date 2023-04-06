import unittest
from test import support
import operator
import test_index

def test_slice():
    BaseTestCase.o.ind = 1
    BaseTestCase.o2.ind = 3
    BaseTestCase.n.ind = 2
    BaseTestCase.n2.ind = 4
    BaseTestCase.assertEqual(BaseTestCase.seq[BaseTestCase.o:BaseTestCase.o2], BaseTestCase.seq[1:3])
    BaseTestCase.assertEqual(BaseTestCase.seq[BaseTestCase.n:BaseTestCase.n2], BaseTestCase.seq[2:4])

BaseTestCase = test_index.BaseTestCase()
BaseTestCase.setUp()
test_slice()
