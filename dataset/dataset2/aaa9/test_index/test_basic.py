import unittest
from test import support
import operator
import test_index

def test_basic():
    BaseTestCase.o.ind = -2
    BaseTestCase.n.ind = 2
    BaseTestCase.assertEqual(operator.index(BaseTestCase.o), -2)
    BaseTestCase.assertEqual(operator.index(BaseTestCase.n), 2)

BaseTestCase = test_index.BaseTestCase()
BaseTestCase.setUp()
test_basic()
