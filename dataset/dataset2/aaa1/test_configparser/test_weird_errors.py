import collections
import configparser
import io
import os
import pathlib
import textwrap
import unittest
import warnings
from test import support
from test.support import os_helper
import decimal
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import decimal
import test_configparser

def test_weird_errors():
    cf = BasicTestCase.newconfig()
    cf.add_section('Foo')
    with BasicTestCase.assertRaises(configparser.DuplicateSectionError) as cm:
        cf.add_section('Foo')
    e = cm.exception
    BasicTestCase.assertEqual(str(e), "Section 'Foo' already exists")
    BasicTestCase.assertEqual(e.args, ('Foo', None, None))
    if BasicTestCase.strict:
        with BasicTestCase.assertRaises(configparser.DuplicateSectionError) as cm:
            cf.read_string(textwrap.dedent("                    [Foo]\n                    will this be added{equals}True\n                    [Bar]\n                    what about this{equals}True\n                    [Foo]\n                    oops{equals}this won't\n                ".format(equals=BasicTestCase.delimiters[0])), source='<foo-bar>')
        e = cm.exception
        BasicTestCase.assertEqual(str(e), "While reading from '<foo-bar>' [line  5]: section 'Foo' already exists")
        BasicTestCase.assertEqual(e.args, ('Foo', '<foo-bar>', 5))
        with BasicTestCase.assertRaises(configparser.DuplicateOptionError) as cm:
            cf.read_dict({'Bar': {'opt': 'val', 'OPT': 'is really `opt`'}})
        e = cm.exception
        BasicTestCase.assertEqual(str(e), "While reading from '<dict>': option 'opt' in section 'Bar' already exists")
        BasicTestCase.assertEqual(e.args, ('Bar', 'opt', '<dict>', None))

BasicTestCase = test_configparser.BasicTestCase()
test_weird_errors()
