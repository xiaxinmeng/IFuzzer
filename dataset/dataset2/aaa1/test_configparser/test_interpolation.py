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

def test_interpolation():
    cf = ConfigParserTestCase.get_interpolation_config()
    eq = ConfigParserTestCase.assertEqual
    eq(cf.get('Foo', 'bar'), 'something %(with1)s interpolation (1 step)')
    eq(cf.get('Foo', 'bar9'), 'something %(with9)s lots of interpolation (9 steps)')
    eq(cf.get('Foo', 'bar10'), 'something %(with10)s lots of interpolation (10 steps)')
    eq(cf.get('Foo', 'bar11'), 'something %(with11)s lots of interpolation (11 steps)')

ConfigParserTestCase = test_configparser.ConfigParserTestCase()
test_interpolation()
