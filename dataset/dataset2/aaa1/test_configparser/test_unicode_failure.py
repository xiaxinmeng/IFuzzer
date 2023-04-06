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

def test_unicode_failure():
    tricky = support.findfile('cfgparser.3')
    cf = ConfigParserTestCaseTrickyFile.newconfig()
    with ConfigParserTestCaseTrickyFile.assertRaises(UnicodeDecodeError):
        cf.read(tricky, encoding='ascii')

ConfigParserTestCaseTrickyFile = test_configparser.ConfigParserTestCaseTrickyFile()
test_unicode_failure()
