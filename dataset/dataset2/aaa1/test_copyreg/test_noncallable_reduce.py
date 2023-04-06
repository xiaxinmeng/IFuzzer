import copyreg
import unittest
from test.pickletester import ExtensionSaver
import copy
import test_copyreg

def test_noncallable_reduce():
    CopyRegTestCase.assertRaises(TypeError, copyreg.pickle, type(1), 'not a callable')

CopyRegTestCase = test_copyreg.CopyRegTestCase()
test_noncallable_reduce()
