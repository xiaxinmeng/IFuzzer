import symtable
import unittest
import test_symtable

def test_nested():
    SymtableTest.assertFalse(SymtableTest.top.is_nested())
    SymtableTest.assertFalse(SymtableTest.Mine.is_nested())
    SymtableTest.assertFalse(SymtableTest.spam.is_nested())
    SymtableTest.assertTrue(SymtableTest.internal.is_nested())

SymtableTest = test_symtable.SymtableTest()
test_nested()
