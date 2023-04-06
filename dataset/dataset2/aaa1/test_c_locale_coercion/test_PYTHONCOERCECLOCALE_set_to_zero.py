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

def test_PYTHONCOERCECLOCALE_set_to_zero():
    LocaleCoercionTests._check_c_locale_coercion(test_c_locale_coercion.EXPECTED_C_LOCALE_FS_ENCODING, test_c_locale_coercion.EXPECTED_C_LOCALE_STREAM_ENCODING, coerce_c_locale='0', coercion_expected=False)
    LocaleCoercionTests._check_c_locale_coercion(test_c_locale_coercion.EXPECTED_C_LOCALE_FS_ENCODING, test_c_locale_coercion.EXPECTED_C_LOCALE_STREAM_ENCODING, coerce_c_locale='0', LC_ALL='C', coercion_expected=False)

LocaleCoercionTests = test_c_locale_coercion.LocaleCoercionTests()
test_PYTHONCOERCECLOCALE_set_to_zero()
