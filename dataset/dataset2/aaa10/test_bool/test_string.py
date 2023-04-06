import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_string():
    BoolTest.assertIs('xyz'.endswith('z'), True)
    BoolTest.assertIs('xyz'.endswith('x'), False)
    BoolTest.assertIs('xyz0123'.isalnum(), True)
    BoolTest.assertIs('@#$%'.isalnum(), False)
    BoolTest.assertIs('xyz'.isalpha(), True)
    BoolTest.assertIs('@#$%'.isalpha(), False)
    BoolTest.assertIs('0123'.isdigit(), True)
    BoolTest.assertIs('xyz'.isdigit(), False)
    BoolTest.assertIs('xyz'.islower(), True)
    BoolTest.assertIs('XYZ'.islower(), False)
    BoolTest.assertIs('0123'.isdecimal(), True)
    BoolTest.assertIs('xyz'.isdecimal(), False)
    BoolTest.assertIs('0123'.isnumeric(), True)
    BoolTest.assertIs('xyz'.isnumeric(), False)
    BoolTest.assertIs(' '.isspace(), True)
    BoolTest.assertIs('\xa0'.isspace(), True)
    BoolTest.assertIs('\u3000'.isspace(), True)
    BoolTest.assertIs('XYZ'.isspace(), False)
    BoolTest.assertIs('X'.istitle(), True)
    BoolTest.assertIs('x'.istitle(), False)
    BoolTest.assertIs('XYZ'.isupper(), True)
    BoolTest.assertIs('xyz'.isupper(), False)
    BoolTest.assertIs('xyz'.startswith('x'), True)
    BoolTest.assertIs('xyz'.startswith('z'), False)

BoolTest = test_bool.BoolTest()
test_string()
