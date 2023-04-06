import copyreg
import unittest
from test.pickletester import ExtensionSaver
import copy
import test_copyreg

def test_noncallable_constructor():
    CopyRegTestCase.assertRaises(TypeError, copyreg.pickle, type(1), int, 'not a callable')

CopyRegTestCase = test_copyreg.CopyRegTestCase()
test_noncallable_constructor()
