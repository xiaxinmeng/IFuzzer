import symtable
import unittest
import test_symtable

def test_symtable_repr():
    SymtableTest.assertEqual(str(SymtableTest.top), '<SymbolTable for module ?>')
    SymtableTest.assertEqual(str(SymtableTest.spam), '<Function SymbolTable for spam in ?>')

SymtableTest = test_symtable.SymtableTest()
test_symtable_repr()
