import unittest
from test import support
import operator
import test_index

def test_wrappers():
    BaseTestCase.o.ind = 4
    BaseTestCase.n.ind = 5
    BaseTestCase.assertEqual(BaseTestCase.seq.__getitem__(BaseTestCase.o), BaseTestCase.seq[4])
    BaseTestCase.assertEqual(BaseTestCase.seq.__mul__(BaseTestCase.o), BaseTestCase.seq * 4)
    BaseTestCase.assertEqual(BaseTestCase.seq.__rmul__(BaseTestCase.o), BaseTestCase.seq * 4)
    BaseTestCase.assertEqual(BaseTestCase.seq.__getitem__(BaseTestCase.n), BaseTestCase.seq[5])
    BaseTestCase.assertEqual(BaseTestCase.seq.__mul__(BaseTestCase.n), BaseTestCase.seq * 5)
    BaseTestCase.assertEqual(BaseTestCase.seq.__rmul__(BaseTestCase.n), BaseTestCase.seq * 5)

BaseTestCase = test_index.BaseTestCase()
BaseTestCase.setUp()
test_wrappers()
