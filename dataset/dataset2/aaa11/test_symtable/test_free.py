import symtable
import unittest
import test_symtable

def test_free():
    SymtableTest.assertTrue(SymtableTest.internal.lookup('x').is_free())

SymtableTest = test_symtable.SymtableTest()
test_free()
