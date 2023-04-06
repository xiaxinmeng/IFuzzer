import symtable
import unittest
import test_symtable

def test_nonlocal():
    SymtableTest.assertFalse(SymtableTest.spam.lookup('some_var').is_nonlocal())
    SymtableTest.assertTrue(SymtableTest.other_internal.lookup('some_var').is_nonlocal())
    expected = ('some_var',)
    SymtableTest.assertEqual(SymtableTest.other_internal.get_nonlocals(), expected)

SymtableTest = test_symtable.SymtableTest()
test_nonlocal()
