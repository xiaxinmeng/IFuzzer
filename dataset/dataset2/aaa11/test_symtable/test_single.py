import symtable
import unittest
import test_symtable

def test_single():
    symbols = symtable.symtable('42', '?', 'single')

SymtableTest = test_symtable.SymtableTest()
test_single()
