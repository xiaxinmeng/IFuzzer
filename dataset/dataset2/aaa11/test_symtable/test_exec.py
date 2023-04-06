import symtable
import unittest
import test_symtable

def test_exec():
    symbols = symtable.symtable('def f(x): return x', '?', 'exec')

SymtableTest = test_symtable.SymtableTest()
test_exec()
