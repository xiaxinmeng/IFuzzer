import unittest
from test import support
import operator
import test_index

def test_setdelitem():
    ListTestCase.o.ind = -2
    ListTestCase.n.ind = 2
    lst = list('ab!cdefghi!j')
    del lst[ListTestCase.o]
    del lst[ListTestCase.n]
    lst[ListTestCase.o] = 'X'
    lst[ListTestCase.n] = 'Y'
    ListTestCase.assertEqual(lst, list('abYdefghXj'))
    lst = [5, 6, 7, 8, 9, 10, 11]
    lst.__setitem__(ListTestCase.n, 'here')
    ListTestCase.assertEqual(lst, [5, 6, 'here', 8, 9, 10, 11])
    lst.__delitem__(ListTestCase.n)
    ListTestCase.assertEqual(lst, [5, 6, 8, 9, 10, 11])

ListTestCase = test_index.ListTestCase()
ListTestCase.setUp()
test_setdelitem()
