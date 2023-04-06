import symtable
import unittest
import test_symtable

def test_assigned():
    SymtableTest.assertTrue(SymtableTest.spam.lookup('x').is_assigned())
    SymtableTest.assertTrue(SymtableTest.spam.lookup('bar').is_assigned())
    SymtableTest.assertTrue(SymtableTest.top.lookup('spam').is_assigned())
    SymtableTest.assertTrue(SymtableTest.Mine.lookup('a_method').is_assigned())
    SymtableTest.assertFalse(SymtableTest.internal.lookup('x').is_assigned())

SymtableTest = test_symtable.SymtableTest()
test_assigned()
