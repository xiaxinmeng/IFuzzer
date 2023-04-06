import symtable
import unittest
import test_symtable

def test_annotated():
    st1 = symtable.symtable('def f():\n    x: int\n', 'test', 'exec')
    st2 = st1.get_children()[0]
    SymtableTest.assertTrue(st2.lookup('x').is_local())
    SymtableTest.assertTrue(st2.lookup('x').is_annotated())
    SymtableTest.assertFalse(st2.lookup('x').is_global())
    st3 = symtable.symtable('def f():\n    x = 1\n', 'test', 'exec')
    st4 = st3.get_children()[0]
    SymtableTest.assertTrue(st4.lookup('x').is_local())
    SymtableTest.assertFalse(st4.lookup('x').is_annotated())
    st5 = symtable.symtable('global x\nx: int', 'test', 'exec')
    SymtableTest.assertTrue(st5.lookup('x').is_global())
    st6 = symtable.symtable('def g():\n    x = 2\n    def f():\n        nonlocal x\n    x: int', 'test', 'exec')

SymtableTest = test_symtable.SymtableTest()
test_annotated()
