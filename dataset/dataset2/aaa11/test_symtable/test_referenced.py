import symtable
import unittest
import test_symtable

def test_referenced():
    SymtableTest.assertTrue(SymtableTest.internal.lookup('x').is_referenced())
    SymtableTest.assertTrue(SymtableTest.spam.lookup('internal').is_referenced())
    SymtableTest.assertFalse(SymtableTest.spam.lookup('x').is_referenced())

SymtableTest = test_symtable.SymtableTest()
test_referenced()
