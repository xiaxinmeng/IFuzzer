import sys
import unittest
from test.support import import_helper
from collections import UserList
from random import randrange
from random import shuffle
from random import choice
import test_bisect

def test_listDerived():

    class List(list):
        data = []

        def insert(TestInsort, index, item):
            TestInsort.data.insert(index, item)
    lst = List()
    TestInsort.module.insort_left(lst, 10)
    TestInsort.module.insort_right(lst, 5)
    TestInsort.assertEqual([5, 10], lst.data)

TestInsort = test_bisect.TestInsort()
test_listDerived()
