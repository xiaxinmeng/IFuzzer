import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_sane_len():
    for badval in ['illegal', -1, 1 << 32]:

        class A:

            def __len__(BoolTest):
                return badval
        try:
            bool(A())
        except Exception as e_bool:
            try:
                len(A())
            except Exception as e_len:
                BoolTest.assertEqual(str(e_bool), str(e_len))

BoolTest = test_bool.BoolTest()
test_sane_len()
