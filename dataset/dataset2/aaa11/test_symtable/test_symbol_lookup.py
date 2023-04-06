import symtable
import unittest
import test_symtable

def test_symbol_lookup():
    SymtableTest.assertEqual(len(SymtableTest.top.get_identifiers()), len(SymtableTest.top.get_symbols()))
    SymtableTest.assertRaises(KeyError, SymtableTest.top.lookup, 'not_here')

SymtableTest = test_symtable.SymtableTest()
test_symbol_lookup()
