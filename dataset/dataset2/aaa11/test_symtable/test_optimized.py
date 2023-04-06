import symtable
import unittest
import test_symtable

def test_optimized():
    SymtableTest.assertFalse(SymtableTest.top.is_optimized())
    SymtableTest.assertTrue(SymtableTest.spam.is_optimized())

SymtableTest = test_symtable.SymtableTest()
test_optimized()
