import symtable
import unittest
import test_symtable

def test_eval():
    symbols = symtable.symtable('42', '?', 'eval')

SymtableTest = test_symtable.SymtableTest()
test_eval()
