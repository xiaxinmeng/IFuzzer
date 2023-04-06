import symtable
import unittest
import test_symtable

def test_imported():
    SymtableTest.assertTrue(SymtableTest.top.lookup('sys').is_imported())

SymtableTest = test_symtable.SymtableTest()
test_imported()
