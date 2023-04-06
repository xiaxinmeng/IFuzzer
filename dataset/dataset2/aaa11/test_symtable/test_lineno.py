import symtable
import unittest
import test_symtable

def test_lineno():
    SymtableTest.assertEqual(SymtableTest.top.get_lineno(), 0)
    SymtableTest.assertEqual(SymtableTest.spam.get_lineno(), 14)

SymtableTest = test_symtable.SymtableTest()
test_lineno()
