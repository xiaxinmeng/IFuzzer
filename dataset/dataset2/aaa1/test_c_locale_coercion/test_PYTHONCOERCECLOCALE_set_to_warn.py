import locale
import os
import subprocess
import sys
import sysconfig
import unittest
from collections import namedtuple
from test import support
from test.support.script_helper import run_python_until_end
import test_c_locale_coercion

def test_PYTHONCOERCECLOCALE_set_to_warn():
    LocaleCoercionTests._check_c_locale_coercion('utf-8', 'utf-8', coerce_c_locale='warn', expected_warnings=[test_c_locale_coercion.CLI_COERCION_WARNING])

LocaleCoercionTests = test_c_locale_coercion.LocaleCoercionTests()
test_PYTHONCOERCECLOCALE_set_to_warn()
