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

def test_PYTHONCOERCECLOCALE_not_zero():
    for setting in ('', '1', 'true', 'false'):
        LocaleCoercionTests._check_c_locale_coercion('utf-8', 'utf-8', coerce_c_locale=setting)

LocaleCoercionTests = test_c_locale_coercion.LocaleCoercionTests()
test_PYTHONCOERCECLOCALE_not_zero()
