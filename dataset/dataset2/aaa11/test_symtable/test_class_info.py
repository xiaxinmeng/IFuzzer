import symtable
import unittest
import test_symtable

def test_class_info():
    SymtableTest.assertEqual(SymtableTest.Mine.get_methods(), ('a_method',))

SymtableTest = test_symtable.SymtableTest()
test_class_info()
