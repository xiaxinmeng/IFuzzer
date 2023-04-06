import symtable
import unittest
import test_symtable

def test_namespaces():
    SymtableTest.assertTrue(SymtableTest.top.lookup('Mine').is_namespace())
    SymtableTest.assertTrue(SymtableTest.Mine.lookup('a_method').is_namespace())
    SymtableTest.assertTrue(SymtableTest.top.lookup('spam').is_namespace())
    SymtableTest.assertTrue(SymtableTest.spam.lookup('internal').is_namespace())
    SymtableTest.assertTrue(SymtableTest.top.lookup('namespace_test').is_namespace())
    SymtableTest.assertFalse(SymtableTest.spam.lookup('x').is_namespace())
    SymtableTest.assertTrue(SymtableTest.top.lookup('spam').get_namespace() is SymtableTest.spam)
    ns_test = SymtableTest.top.lookup('namespace_test')
    SymtableTest.assertEqual(len(ns_test.get_namespaces()), 2)
    SymtableTest.assertRaises(ValueError, ns_test.get_namespace)

SymtableTest = test_symtable.SymtableTest()
test_namespaces()
