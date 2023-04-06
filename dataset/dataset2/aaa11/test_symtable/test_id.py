import symtable
import unittest
import test_symtable

def test_id():
    SymtableTest.assertGreater(SymtableTest.top.get_id(), 0)
    SymtableTest.assertGreater(SymtableTest.Mine.get_id(), 0)
    SymtableTest.assertGreater(SymtableTest.a_method.get_id(), 0)
    SymtableTest.assertGreater(SymtableTest.spam.get_id(), 0)
    SymtableTest.assertGreater(SymtableTest.internal.get_id(), 0)

SymtableTest = test_symtable.SymtableTest()
test_id()
