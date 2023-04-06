import symtable
import unittest
import test_symtable

def test_parameters():
    for sym in ('a', 'var', 'kw'):
        SymtableTest.assertTrue(SymtableTest.spam.lookup(sym).is_parameter())
    SymtableTest.assertFalse(SymtableTest.spam.lookup('x').is_parameter())

SymtableTest = test_symtable.SymtableTest()
test_parameters()
