import symtable
import unittest
import test_symtable

def test_name():
    SymtableTest.assertEqual(SymtableTest.top.get_name(), 'top')
    SymtableTest.assertEqual(SymtableTest.spam.get_name(), 'spam')
    SymtableTest.assertEqual(SymtableTest.spam.lookup('x').get_name(), 'x')
    SymtableTest.assertEqual(SymtableTest.Mine.get_name(), 'Mine')

SymtableTest = test_symtable.SymtableTest()
test_name()
