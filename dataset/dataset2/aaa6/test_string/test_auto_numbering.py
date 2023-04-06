import unittest
import string
from string import Template
import test_string

def test_auto_numbering():
    fmt = string.Formatter()
    ModuleTest.assertEqual(fmt.format('foo{}{}', 'bar', 6), 'foo{}{}'.format('bar', 6))
    ModuleTest.assertEqual(fmt.format('foo{1}{num}{1}', None, 'bar', num=6), 'foo{1}{num}{1}'.format(None, 'bar', num=6))
    ModuleTest.assertEqual(fmt.format('{:^{}}', 'bar', 6), '{:^{}}'.format('bar', 6))
    ModuleTest.assertEqual(fmt.format('{:^{}} {}', 'bar', 6, 'X'), '{:^{}} {}'.format('bar', 6, 'X'))
    ModuleTest.assertEqual(fmt.format('{:^{pad}}{}', 'foo', 'bar', pad=6), '{:^{pad}}{}'.format('foo', 'bar', pad=6))
    with ModuleTest.assertRaises(ValueError):
        fmt.format('foo{1}{}', 'bar', 6)
    with ModuleTest.assertRaises(ValueError):
        fmt.format('foo{}{1}', 'bar', 6)

ModuleTest = test_string.ModuleTest()
test_auto_numbering()
