import unittest
from test import support
import operator
import test_index

def test_inplace_repeat():
    ListTestCase.o.ind = 2
    ListTestCase.n.ind = 3
    lst = [6, 4]
    lst *= ListTestCase.o
    ListTestCase.assertEqual(lst, [6, 4, 6, 4])
    lst *= ListTestCase.n
    ListTestCase.assertEqual(lst, [6, 4, 6, 4] * 3)
    lst = [5, 6, 7, 8, 9, 11]
    l2 = lst.__imul__(ListTestCase.n)
    ListTestCase.assertIs(l2, lst)
    ListTestCase.assertEqual(lst, [5, 6, 7, 8, 9, 11] * 3)

ListTestCase = test_index.ListTestCase()
ListTestCase.setUp()
test_inplace_repeat()
