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

def test_other_errors():
    cf = ConfigParserTestCaseExtendedInterpolation.fromstring("\n            [interpolation fail]\n            case1 = ${where's the brace\n            case2 = ${does_not_exist}\n            case3 = ${wrong_section:wrong_value}\n            case4 = ${i:like:colon:characters}\n            case5 = $100 for Fail No 5!\n        ")
    with ConfigParserTestCaseExtendedInterpolation.assertRaises(configparser.InterpolationSyntaxError):
        cf['interpolation fail']['case1']
    with ConfigParserTestCaseExtendedInterpolation.assertRaises(configparser.InterpolationMissingOptionError):
        cf['interpolation fail']['case2']
    with ConfigParserTestCaseExtendedInterpolation.assertRaises(configparser.InterpolationMissingOptionError):
        cf['interpolation fail']['case3']
    with ConfigParserTestCaseExtendedInterpolation.assertRaises(configparser.InterpolationSyntaxError):
        cf['interpolation fail']['case4']
    with ConfigParserTestCaseExtendedInterpolation.assertRaises(configparser.InterpolationSyntaxError):
        cf['interpolation fail']['case5']
    with ConfigParserTestCaseExtendedInterpolation.assertRaises(ValueError):
        cf['interpolation fail']['case6'] = 'BLACK $ABBATH'

ConfigParserTestCaseExtendedInterpolation = test_configparser.ConfigParserTestCaseExtendedInterpolation()
test_other_errors()
