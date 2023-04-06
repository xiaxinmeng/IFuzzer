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

def test_basic_from_dict():
    config = {'Foo Bar': {'foo': 'bar1'}, 'Spacey Bar': {'foo': 'bar2'}, 'Spacey Bar From The Beginning': {'foo': 'bar3', 'baz': 'qwe'}, 'Commented Bar': {'foo': 'bar4', 'baz': 'qwe'}, 'Long Line': {'foo': 'this line is much, much longer than my editor\nlikes it.'}, 'Section\\with$weird%characters[\t': {}, 'Internationalized Stuff': {'foo[bg]': 'Bulgarian', 'foo': 'Default', 'foo[en]': 'English', 'foo[de]': 'Deutsch'}, 'Spaces': {'key with spaces': 'value', 'another with spaces': 'splat!'}, 'Types': {'int': 42, 'float': 0.44, 'boolean': False, 123: 'strange but acceptable'}}
    if BasicTestCase.allow_no_value:
        config.update({'NoValue': {'option-without-value': None}})
    cf = BasicTestCase.newconfig()
    cf.read_dict(config)
    BasicTestCase.basic_test(cf)
    if BasicTestCase.strict:
        with BasicTestCase.assertRaises(configparser.DuplicateSectionError):
            cf.read_dict({'1': {'key': 'value'}, 1: {'key2': 'value2'}})
        with BasicTestCase.assertRaises(configparser.DuplicateOptionError):
            cf.read_dict({'Duplicate Options Here': {'option': 'with a value', 'OPTION': 'with another value'}})
    else:
        cf.read_dict({'section': {'key': 'value'}, 'SECTION': {'key2': 'value2'}})
        cf.read_dict({'Duplicate Options Here': {'option': 'with a value', 'OPTION': 'with another value'}})

BasicTestCase = test_configparser.BasicTestCase()
test_basic_from_dict()
