import unittest
from test import support
import operator
import test_index

def test_subclasses():
    BaseTestCase.assertEqual(BaseTestCase.seq[TrapInt()], BaseTestCase.seq[0])

BaseTestCase = test_index.BaseTestCase()
BaseTestCase.setUp()
test_subclasses()
