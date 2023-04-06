import unittest
import string
from string import Template
import test_string

def test_override_get_value():

    class NamespaceFormatter(string.Formatter):

        def __init__(ModuleTest, namespace={}):
            string.Formatter.__init__(ModuleTest)
            ModuleTest.namespace = namespace

        def get_value(ModuleTest, key, args, kwds):
            if isinstance(key, str):
                try:
                    return kwds[key]
                except KeyError:
                    return ModuleTest.namespace[key]
            else:
                string.Formatter.get_value(key, args, kwds)
    fmt = NamespaceFormatter({'greeting': 'hello'})
    ModuleTest.assertEqual(fmt.format('{greeting}, world!'), 'hello, world!')

ModuleTest = test_string.ModuleTest()
test_override_get_value()
