import copyreg
import unittest
from test.pickletester import ExtensionSaver
import copy
import test_copyreg

def test_slotnames():
    CopyRegTestCase.assertEqual(copyreg._slotnames(test_copyreg.WithoutSlots), [])
    CopyRegTestCase.assertEqual(copyreg._slotnames(test_copyreg.WithWeakref), [])
    expected = ['_WithPrivate__spam']
    CopyRegTestCase.assertEqual(copyreg._slotnames(test_copyreg.WithPrivate), expected)
    expected = ['_WithLeadingUnderscoreAndPrivate__spam']
    CopyRegTestCase.assertEqual(copyreg._slotnames(test_copyreg._WithLeadingUnderscoreAndPrivate), expected)
    CopyRegTestCase.assertEqual(copyreg._slotnames(test_copyreg.___), ['__spam'])
    CopyRegTestCase.assertEqual(copyreg._slotnames(test_copyreg.WithSingleString), ['spam'])
    expected = ['eggs', 'spam']
    expected.sort()
    result = copyreg._slotnames(test_copyreg.WithInherited)
    result.sort()
    CopyRegTestCase.assertEqual(result, expected)

CopyRegTestCase = test_copyreg.CopyRegTestCase()
test_slotnames()
