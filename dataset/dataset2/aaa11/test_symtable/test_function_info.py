import symtable
import unittest
import test_symtable

def test_function_info():
    func = SymtableTest.spam
    SymtableTest.assertEqual(sorted(func.get_parameters()), ['a', 'b', 'kw', 'var'])
    expected = ['a', 'b', 'internal', 'kw', 'other_internal', 'some_var', 'var', 'x']
    SymtableTest.assertEqual(sorted(func.get_locals()), expected)
    SymtableTest.assertEqual(sorted(func.get_globals()), ['bar', 'glob', 'some_assigned_global_var'])
    SymtableTest.assertEqual(SymtableTest.internal.get_frees(), ('x',))

SymtableTest = test_symtable.SymtableTest()
test_function_info()
