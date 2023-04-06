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

def test_set_string_types():
    cf = BasicTestCase.fromstring('[sect]\noption1{eq}foo\n'.format(eq=BasicTestCase.delimiters[0]))

    class mystr(str):
        pass
    cf.set('sect', 'option1', 'splat')
    cf.set('sect', 'option1', mystr('splat'))
    cf.set('sect', 'option2', 'splat')
    cf.set('sect', 'option2', mystr('splat'))
    cf.set('sect', 'option1', 'splat')
    cf.set('sect', 'option2', 'splat')

BasicTestCase = test_configparser.BasicTestCase()
test_set_string_types()
