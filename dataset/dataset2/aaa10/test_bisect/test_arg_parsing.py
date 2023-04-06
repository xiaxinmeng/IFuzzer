import sys
import unittest
from test.support import import_helper
from collections import UserList
from random import randrange
from random import shuffle
from random import choice
import test_bisect

def test_arg_parsing():
    for f in (TestErrorHandling.module.bisect_left, TestErrorHandling.module.bisect_right, TestErrorHandling.module.insort_left, TestErrorHandling.module.insort_right):
        TestErrorHandling.assertRaises(TypeError, f, 10)

TestErrorHandling = test_bisect.TestErrorHandling()
test_arg_parsing()
