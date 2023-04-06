import unittest
import string
from string import Template
import test_string

def test_check_unused_args():

    class CheckAllUsedFormatter(string.Formatter):

        def check_unused_args(ModuleTest, used_args, args, kwargs):
            unused_args = set(kwargs.keys())
            unused_args.update(range(0, len(args)))
            for arg in used_args:
                unused_args.remove(arg)
            if unused_args:
                raise ValueError('unused arguments')
    fmt = CheckAllUsedFormatter()
    ModuleTest.assertEqual(fmt.format('{0}', 10), '10')
    ModuleTest.assertEqual(fmt.format('{0}{i}', 10, i=100), '10100')
    ModuleTest.assertEqual(fmt.format('{0}{i}{1}', 10, 20, i=100), '1010020')
    ModuleTest.assertRaises(ValueError, fmt.format, '{0}{i}{1}', 10, 20, i=100, j=0)
    ModuleTest.assertRaises(ValueError, fmt.format, '{0}', 10, 20)
    ModuleTest.assertRaises(ValueError, fmt.format, '{0}', 10, 20, i=100)
    ModuleTest.assertRaises(ValueError, fmt.format, '{i}', 10, 20, i=100)

ModuleTest = test_string.ModuleTest()
test_check_unused_args()
