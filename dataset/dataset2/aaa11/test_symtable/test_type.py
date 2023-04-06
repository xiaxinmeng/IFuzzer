import symtable
import unittest
import test_symtable

def test_type():
    SymtableTest.assertEqual(SymtableTest.top.get_type(), 'module')
    SymtableTest.assertEqual(SymtableTest.Mine.get_type(), 'class')
    SymtableTest.assertEqual(SymtableTest.a_method.get_type(), 'function')
    SymtableTest.assertEqual(SymtableTest.spam.get_type(), 'function')
    SymtableTest.assertEqual(SymtableTest.internal.get_type(), 'function')

SymtableTest = test_symtable.SymtableTest()
test_type()
