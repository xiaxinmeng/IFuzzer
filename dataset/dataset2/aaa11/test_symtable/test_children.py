import symtable
import unittest
import test_symtable

def test_children():
    SymtableTest.assertTrue(SymtableTest.top.has_children())
    SymtableTest.assertTrue(SymtableTest.Mine.has_children())
    SymtableTest.assertFalse(SymtableTest.foo.has_children())

SymtableTest = test_symtable.SymtableTest()
test_children()
