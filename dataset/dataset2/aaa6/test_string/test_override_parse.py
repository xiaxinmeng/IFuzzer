import unittest
import string
from string import Template
import test_string

def test_override_parse():

    class BarFormatter(string.Formatter):

        def parse(ModuleTest, format_string):
            for field in format_string.split('|'):
                if field[0] == '+':
                    (field_name, _, format_spec) = field[1:].partition(':')
                    yield ('', field_name, format_spec, None)
                else:
                    yield (field, None, None, None)
    fmt = BarFormatter()
    ModuleTest.assertEqual(fmt.format('*|+0:^10s|*', 'foo'), '*   foo    *')

ModuleTest = test_string.ModuleTest()
test_override_parse()
