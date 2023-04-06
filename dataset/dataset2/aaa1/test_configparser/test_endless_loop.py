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

def test_endless_loop():
    cf = ConfigParserTestCaseExtendedInterpolation.fromstring(textwrap.dedent('\n            [one for you]\n            ping = ${one for me:pong}\n\n            [one for me]\n            pong = ${one for you:ping}\n\n            [ConfigParserTestCaseExtendedInterpolationish]\n            me = ${me}\n        ').strip())
    with ConfigParserTestCaseExtendedInterpolation.assertRaises(configparser.InterpolationDepthError):
        cf['one for you']['ping']
    with ConfigParserTestCaseExtendedInterpolation.assertRaises(configparser.InterpolationDepthError):
        cf['ConfigParserTestCaseExtendedInterpolationish']['me']

ConfigParserTestCaseExtendedInterpolation = test_configparser.ConfigParserTestCaseExtendedInterpolation()
test_endless_loop()
