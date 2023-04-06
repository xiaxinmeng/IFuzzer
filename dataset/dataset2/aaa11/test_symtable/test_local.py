import symtable
import unittest
import test_symtable

def test_local():
    SymtableTest.assertTrue(SymtableTest.spam.lookup('x').is_local())
    SymtableTest.assertFalse(SymtableTest.spam.lookup('bar').is_local())
    SymtableTest.assertTrue(SymtableTest.top.lookup('some_non_assigned_global_var').is_local())
    SymtableTest.assertTrue(SymtableTest.top.lookup('some_assigned_global_var').is_local())

SymtableTest = test_symtable.SymtableTest()
test_local()
