import symtable
import unittest
import test_symtable

def test_globals():
    SymtableTest.assertTrue(SymtableTest.spam.lookup('glob').is_global())
    SymtableTest.assertFalse(SymtableTest.spam.lookup('glob').is_declared_global())
    SymtableTest.assertTrue(SymtableTest.spam.lookup('bar').is_global())
    SymtableTest.assertTrue(SymtableTest.spam.lookup('bar').is_declared_global())
    SymtableTest.assertFalse(SymtableTest.internal.lookup('x').is_global())
    SymtableTest.assertFalse(SymtableTest.Mine.lookup('instance_var').is_global())
    SymtableTest.assertTrue(SymtableTest.spam.lookup('bar').is_global())
    SymtableTest.assertTrue(SymtableTest.top.lookup('some_non_assigned_global_var').is_global())
    SymtableTest.assertTrue(SymtableTest.top.lookup('some_assigned_global_var').is_global())

SymtableTest = test_symtable.SymtableTest()
test_globals()
