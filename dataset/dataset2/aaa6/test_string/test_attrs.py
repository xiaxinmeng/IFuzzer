import unittest
import string
from string import Template
import test_string

def test_attrs():
    ModuleTest.assertEqual(string.whitespace, ' \t\n\r\x0b\x0c')
    ModuleTest.assertEqual(string.ascii_lowercase, 'abcdefghijklmnopqrstuvwxyz')
    ModuleTest.assertEqual(string.ascii_uppercase, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ModuleTest.assertEqual(string.ascii_letters, string.ascii_lowercase + string.ascii_uppercase)
    ModuleTest.assertEqual(string.digits, '0123456789')
    ModuleTest.assertEqual(string.hexdigits, string.digits + 'abcdefABCDEF')
    ModuleTest.assertEqual(string.octdigits, '01234567')
    ModuleTest.assertEqual(string.punctuation, '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    ModuleTest.assertEqual(string.printable, string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.whitespace)

ModuleTest = test_string.ModuleTest()
test_attrs()
