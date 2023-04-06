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

def test_strange_options():
    cf = ConfigParserTestCaseExtendedInterpolation.fromstring('\n            [dollars]\n            $var = $$value\n            $var2 = ${$var}\n            ${sick} = cannot interpolate me\n\n            [interpolated]\n            $other = ${dollars:$var}\n            $trying = ${dollars:${sick}}\n        ')
    ConfigParserTestCaseExtendedInterpolation.assertEqual(cf['dollars']['$var'], '$value')
    ConfigParserTestCaseExtendedInterpolation.assertEqual(cf['interpolated']['$other'], '$value')
    ConfigParserTestCaseExtendedInterpolation.assertEqual(cf['dollars']['${sick}'], 'cannot interpolate me')
    exception_class = configparser.InterpolationMissingOptionError
    with ConfigParserTestCaseExtendedInterpolation.assertRaises(exception_class) as cm:
        cf['interpolated']['$trying']
    ConfigParserTestCaseExtendedInterpolation.assertEqual(cm.exception.reference, 'dollars:${sick')
    ConfigParserTestCaseExtendedInterpolation.assertEqual(cm.exception.args[2], '${dollars:${sick}}')

ConfigParserTestCaseExtendedInterpolation = test_configparser.ConfigParserTestCaseExtendedInterpolation()
test_strange_options()
