import unittest
import string
from string import Template
import test_string

def test_capwords():
    ModuleTest.assertEqual(string.capwords('abc def ghi'), 'Abc Def Ghi')
    ModuleTest.assertEqual(string.capwords('abc\tdef\nghi'), 'Abc Def Ghi')
    ModuleTest.assertEqual(string.capwords('abc\t   def  \nghi'), 'Abc Def Ghi')
    ModuleTest.assertEqual(string.capwords('ABC DEF GHI'), 'Abc Def Ghi')
    ModuleTest.assertEqual(string.capwords('ABC-DEF-GHI', '-'), 'Abc-Def-Ghi')
    ModuleTest.assertEqual(string.capwords('ABC-def DEF-ghi GHI'), 'Abc-def Def-ghi Ghi')
    ModuleTest.assertEqual(string.capwords('   aBc  DeF   '), 'Abc Def')
    ModuleTest.assertEqual(string.capwords('\taBc\tDeF\t'), 'Abc Def')
    ModuleTest.assertEqual(string.capwords('\taBc\tDeF\t', '\t'), '\tAbc\tDef\t')

ModuleTest = test_string.ModuleTest()
test_capwords()
