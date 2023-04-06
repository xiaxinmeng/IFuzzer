import copyreg
import unittest
from test.pickletester import ExtensionSaver
import copy
import test_copyreg

def test_class():
    CopyRegTestCase.assertRaises(TypeError, copyreg.pickle, C, None, None)

CopyRegTestCase = test_copyreg.CopyRegTestCase()
test_class()
